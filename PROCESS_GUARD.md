# chunk-chunk / HMK-9D Process Guard

This repository treats semantic flow as a sequence of explicit transitions rather than one opaque prompt/result pair.

## Core path

```text
chunk_t
→ compression / context transform
→ relation state [x9D]
→ policy / interpretation
→ chunk_t+1
→ observable artifact
```

## Process invariants

- local virtual environments and package-manager state are not source artifacts;
- each semantic bridge must have a declared role rather than silently changing mandate;
- a threshold `‡` is a review / regime transition, not decorative syntax;
- changes to HMK-9D definitions require a corresponding update to examples/specification;
- experimental claims must distinguish `OBSERVED`, `DERIVED`, `ASSUMED` and `HYPOTHESIS`;
- a multi-step chain is reviewed as a trajectory, not only as individually valid chunks.

## `_neuro` / EEG operational mapping

Use the analogy only for process dynamics:

```text
baseline = stable protocol state
burst    = rapid semantic expansion
coupling = bridge activation across chunks
 drift   = state no longer explained by current protocol
recovery = return to a documented, reproducible state
```

## Review loop

```text
baseline
→ semantic delta
→ bridge / threshold mapping
→ falsification probe
→ patch
→ example / artifact regeneration
→ regression check
→ merge
```

The wider cross-repository maintenance contract lives in `DonkeyJJLove/writeups/PROCESS_GUARD.md`.
