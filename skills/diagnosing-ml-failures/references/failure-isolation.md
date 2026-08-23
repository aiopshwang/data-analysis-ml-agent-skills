# Failure Isolation Guide

Use this reference when a failure crosses data, modeling, and runtime boundaries or when multiple causes fit the same symptom.

## Establish a stable comparison

The highest-value diagnostic artifact is a paired comparison with one known difference. Prefer, in order:

1. same record, same artifact, different execution path;
2. same records and code, different data snapshot;
3. same data and environment, different code or artifact;
4. matched cohorts from good and bad time windows;
5. aggregate comparison only when record-level pairing is impossible.

Record the comparison's uncontrolled differences. A "last good" run is useful only if its data, code, configuration, artifact, and metric identity can be established.

## Probe boundaries with invariants

| Layer | High-signal invariants |
|---|---|
| Source | snapshot ID, extraction time, schema, row count, key cardinality, time range |
| Join / transform | left/right cardinality, unmatched keys, duplication factor, null deltas, record hashes |
| Labels | definition version, observation cutoff, prevalence, delay, reviewer disagreement |
| Split | entity and time overlap, cohort counts, target prevalence, duplicate fingerprints |
| Features | ordered schema, dtype, missing/default rates, summary distributions, availability time |
| Artifact | checksum, framework version, feature contract, class order, preprocessing state |
| Predictions | record-level score, rank, threshold, abstention and postprocessing |
| Metrics | input population, denominator, grouping, weights, exclusions, confidence interval |
| Runtime | image/dependency hashes, hardware, locale/timezone, concurrency, cache identity |

Trace a few representative records end to end, including a failure, a known-good control, and a boundary case. Aggregate dashboards often hide row duplication, record loss, or class-order reversal.

## Choose discriminating experiments

A useful experiment changes the expected observation for competing hypotheses.

| Pattern | Experiment | Interpretation |
|---|---|---|
| Data versus code | 2x2 swap of old/new data and old/new code | Identifies which axis carries the failure and whether they interact |
| Pipeline parity | Run one frozen artifact and record set through both paths | First divergent intermediate locates the boundary |
| Label defect | Blind independent review of a prespecified error sample | Estimates label error without selecting only favorable cases |
| Metric defect | Recompute from immutable predictions with a minimal implementation | Separates prediction change from reporting change |
| Threshold drift | Compare score distributions and decisions at the locked threshold | Separates discrimination from decision-policy changes |
| State or cache defect | Cold run versus warm run with explicit cache identity | Reveals hidden state while preserving a control |
| Nondeterminism | Repeat unchanged runs and quantify variance | Distinguishes stochastic spread from systematic regression |

Do not change multiple stages and infer cause from recovery. Reverting a bundle identifies a useful recovery action, not which component caused the failure.

## Keep a hypothesis ledger

For each hypothesis, store:

- predicted observations if true and if false;
- the minimal discriminating test;
- evidence identifiers rather than narrative memory;
- result and confidence;
- status: `open`, `supported`, `rejected`, or `blocked`;
- what would reopen a rejected hypothesis.

Negative evidence must remain visible. Delete neither failed experiments nor hypotheses that appeared plausible at the time.

## Validate root-cause closure

Require all four:

1. **Localization:** the first divergent layer is demonstrated.
2. **Mechanism:** the cause explains how that divergence produces the symptom.
3. **Intervention:** changing only the causal factor removes the symptom.
4. **Control:** an unaffected case or invariant remains correct, and a regression check covers the original scope.

If the intervention works but the mechanism remains unknown, classify it as mitigation, not root cause. If only one example is fixed, classify it as example-level evidence, not population-level resolution.
