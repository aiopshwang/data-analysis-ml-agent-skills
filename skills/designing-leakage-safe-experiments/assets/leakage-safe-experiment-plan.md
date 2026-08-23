# Leakage-safe experiment plan

Complete this protocol before model tuning. Amendments made after results are visible belong in the change log.

## Prediction contract

| Field | Definition | Evidence or owner |
|---|---|---|
| Decision and model output |  |  |
| Entity and prediction grain |  |  |
| Eligible population at prediction |  |  |
| Prediction timestamp |  |  |
| Feature cutoff |  |  |
| Outcome and maturity window |  |  |
| Deployment cadence and horizon |  |  |
| Error costs and capacity constraints |  |  |

## Feature availability ledger

| Feature or family | Source event | Event time | Typical availability delay | Corrections or backfills | Earliest production availability | Outcome-dependent? | Eligible? | Evidence |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

## Split protocol

- Deployment claim represented:
- Split type and rationale:
- Split unit:
- Train interval or groups:
- Validation interval or groups:
- Final test interval or groups:
- Gap or embargo:
- Duplicate and dependence controls:
- Test access rule:

## Pipeline boundaries

| Step | Learned from training fold only? | Implementation boundary | Persisted artifact | Leakage check |
|---|---|---|---|---|
| Imputation |  |  |  |  |
| Encoding or vocabulary |  |  |  |  |
| Scaling or normalization |  |  |  |  |
| Feature selection |  |  |  |  |
| Sampling or weighting |  |  |  |  |
| Calibration | separate split or out-of-fold predictions |  |  |  |
| Threshold / decision policy | validation or calibration evidence; never final test |  |  |  |

## Locked comparison

- Simple baseline and why it is credible:
- Primary metric:
- Guardrail metrics:
- Operating threshold or decision rule:
- Uncertainty or variation estimate:
- Required slices:
- Minimum worthwhile improvement:
- Compute or latency budget:

## Planned falsification and stress tests

| Threat | Test capable of revealing it | Pass condition | Result | Disposition |
|---|---|---|---|---|
| Future information |  |  |  |  |
| Cross-fold dependence |  |  |  |  |
| Full-data preprocessing |  |  |  |  |
| Cohort or label maturity |  |  |  |  |
| Suspicious feature proxy |  |  |  |  |
| Temporal or group instability |  |  |  |  |

## Experiment and failure log

| Run ID | Hypothesis | One material change | Frozen data/split ID | Result vs baseline | Slice or stress result | Failure or anomaly | Keep, reject, or investigate |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

## Protocol change log

| Time | Change | Evidence available before change | Reason | Approval if material | New experiment family ID |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Final claim gate

- Untouched evidence used for final claim:
- Result and uncertainty:
- Improvement over baseline:
- Conditions where the claim holds:
- Known failure modes:
- Unresolved leakage risks:
- Reproduction command and artifact identifiers:
