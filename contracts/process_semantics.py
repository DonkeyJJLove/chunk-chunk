from __future__ import annotations
from dataclasses import asdict, dataclass, replace
from hashlib import sha256
import json,re
from typing import Any, Mapping, Sequence

SCHEMA_ID="lion.process-semantics/v1"
AUTHORITY_EFFECT="NONE"
EXECUTION_EFFECT="NONE"
AXES=("T","S","R","E","I","F","A","P","D")
_SHA=re.compile(r"^[0-9a-f]{64}$")
_ID=re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:/-]{0,255}$")
_FIELDS=frozenset({"schema_id","spec_id","source_ref","source_digest","protocol_version","axes","bridge_ids","consumer_refs","runtime_identifier_policy","authority_effect","execution_effect","spec_digest"})

class ProcessSemanticsError(ValueError): pass

def _json(v): return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()

def _ref(v,n):
    if not isinstance(v,str) or _ID.fullmatch(v) is None: raise ProcessSemanticsError(n)
    return v

def _refs(v,n):
    if isinstance(v,(str,bytes)) or not isinstance(v,(list,tuple)): raise ProcessSemanticsError(n)
    out=tuple(_ref(x,n) for x in v)
    if not out or len(out)!=len(set(out)) or out!=tuple(sorted(out)): raise ProcessSemanticsError(n)
    return out

@dataclass(frozen=True)
class ProcessSemanticsSpec:
    schema_id:str
    spec_id:str
    source_ref:str
    source_digest:str
    protocol_version:str
    axes:tuple[str,...]
    bridge_ids:tuple[str,...]
    consumer_refs:tuple[str,...]
    runtime_identifier_policy:str
    authority_effect:str=AUTHORITY_EFFECT
    execution_effect:str=EXECUTION_EFFECT
    spec_digest:str=""

    def payload(self):
        d=asdict(self);d.pop("spec_digest",None);return d
    def compute_digest(self): return sha256(b"LION/PROCESS-SEMANTICS/1\0"+_json(self.payload())).hexdigest()
    def validate(self,require_digest=True):
        if self.schema_id!=SCHEMA_ID: raise ProcessSemanticsError("schema")
        _ref(self.spec_id,"spec_id")
        if not isinstance(self.source_ref,str) or not self.source_ref: raise ProcessSemanticsError("source_ref")
        if not isinstance(self.source_digest,str) or _SHA.fullmatch(self.source_digest) is None: raise ProcessSemanticsError("source_digest")
        if not isinstance(self.protocol_version,str) or not self.protocol_version: raise ProcessSemanticsError("protocol_version")
        if tuple(self.axes)!=AXES: raise ProcessSemanticsError("axes")
        _refs(self.bridge_ids,"bridge_ids");_refs(self.consumer_refs,"consumer_refs")
        if self.runtime_identifier_policy!="INTERNAL_ONLY": raise ProcessSemanticsError("runtime_identifier_policy")
        if self.authority_effect!="NONE" or self.execution_effect!="NONE": raise ProcessSemanticsError("effects")
        if require_digest:
            if not isinstance(self.spec_digest,str) or _SHA.fullmatch(self.spec_digest) is None or self.spec_digest!=self.compute_digest(): raise ProcessSemanticsError("spec_digest")
        return self
    def sealed(self): return replace(self,spec_digest=self.compute_digest()).validate()
    def to_dict(self):
        d=asdict(self);d["axes"]=list(self.axes);d["bridge_ids"]=list(self.bridge_ids);d["consumer_refs"]=list(self.consumer_refs);return d

    @classmethod
    def build(cls,*,spec_id,source_ref,source_digest,protocol_version,bridge_ids:Sequence[str],consumer_refs:Sequence[str]):
        return cls(SCHEMA_ID,spec_id,source_ref,source_digest,protocol_version,AXES,tuple(sorted(bridge_ids)),tuple(sorted(consumer_refs)),"INTERNAL_ONLY").sealed()

def process_semantics_from_mapping(value:Mapping[str,Any])->ProcessSemanticsSpec:
    if not isinstance(value,Mapping) or set(value)!=_FIELDS: raise ProcessSemanticsError("fields")
    d=dict(value)
    for k in ("axes","bridge_ids","consumer_refs"):
        if not isinstance(d[k],(list,tuple)): raise ProcessSemanticsError(k)
        d[k]=tuple(d[k])
    try:return ProcessSemanticsSpec(**d).validate()
    except TypeError as exc: raise ProcessSemanticsError("types") from exc
