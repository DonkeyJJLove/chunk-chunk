from pathlib import Path
import hashlib,json,unittest
from contracts.process_semantics import ProcessSemanticsError,process_semantics_from_mapping
ROOT=Path(__file__).resolve().parents[1]
class ProcessSemanticsTests(unittest.TestCase):
 def load(self): return json.loads((ROOT/"tests/fixtures/process_semantics/hmk9d_minimal.json").read_text())
 def test_fixture_binds_real_protocol_and_consumers(self):
  v=process_semantics_from_mapping(self.load())
  self.assertEqual(v.source_digest,hashlib.sha256((ROOT/v.source_ref).read_bytes()).hexdigest())
  source=(ROOT/v.source_ref).read_text(encoding="utf-8")
  for bridge in v.bridge_ids:self.assertIn('id: "'+bridge+'"',source)
  self.assertEqual(set(v.consumer_refs),{"DonkeyJJLove/ai_platform","DonkeyJJLove/glitchlab"})
 def test_prompt_or_runtime_identifier_does_not_become_execution(self):
  v=process_semantics_from_mapping(self.load())
  self.assertEqual((v.runtime_identifier_policy,v.authority_effect,v.execution_effect),("INTERNAL_ONLY","NONE","NONE"))
 def test_unknown_field_and_effect_widening_fail_closed(self):
  x=self.load();x["unknown"]=1
  with self.assertRaises(ProcessSemanticsError):process_semantics_from_mapping(x)
  x=self.load();x["authority_effect"]="ALLOW"
  with self.assertRaises(ProcessSemanticsError):process_semantics_from_mapping(x)
if __name__=="__main__":unittest.main()
