# Leakage threats and deployment-matched splits

Leakage is any information path that makes evaluation easier than deployment. It includes direct target columns, but also cohort construction, availability timing, cross-fold dependence, preprocessing, and repeated human feedback from the holdout.

## Availability threats

- **Post-outcome data:** events, codes, notes, or actions produced after the target occurs.
- **Delayed recording:** a field has an early event timestamp but was not available until later.
- **Retrospective correction:** current snapshots overwrite the value known at prediction time.
- **Outcome-dependent measurement:** a test or follow-up exists because the outcome was suspected.
- **Proxy identifiers:** status, billing, workflow, or naming fields encode downstream decisions.

Control these with point-in-time reconstruction, explicit feature cutoffs, availability timestamps, suspicious-feature ablations, and production-path simulation.

## Cross-fold dependence

- the same entity or correlated unit appears in train and evaluation;
- duplicates, near-duplicates, document versions, images from one study, or windows from one sequence cross folds;
- sites, operators, households, devices, or campaigns are shared when deployment targets new groups;
- overlapping feature or label windows allow adjacent examples to share future context.

Split at the highest unit that carries dependence and add a temporal gap or embargo when windows overlap.

## Pipeline leakage

Statistics learned from all data leak through imputation, scaling, encoding, feature selection, dimensionality reduction, resampling, calibration, or threshold tuning. Place learned transformations inside the training fold. Deriving a vocabulary, category map, or missingness rule from the full dataset also counts when it uses evaluation information.

Do not fit a calibrator on the same predictions used to fit the base model. Use a separate calibration split or honest out-of-fold predictions. Select thresholds and decision policies from validation or calibration evidence, then leave the final test untouched until every learned component and policy is locked.

## Cohort and label leakage

Retrospective inclusion can depend on completing follow-up, receiving treatment, surviving long enough, or having a known label. This changes the eligible population relative to deployment. Define eligibility using only information available at the prediction event, then apply a separate maturity rule for outcome observation.

## Choose the split from the claim

| Deployment claim | Primary split | Additional challenge |
|---|---|---|
| Future cases from known population | forward temporal holdout | rolling backtest and drift slices |
| New events from known entities | temporal split within entity with embargo | entity-level holdout |
| New entities | grouped holdout by entity | temporal group holdout |
| New sites or regions | site or spatial holdout | leave-one-site-out |
| New source or acquisition system | source holdout | temporal holdout within source |
| IID generalization is genuinely intended | random stratified split | duplicate and dependence audit |

Use nested cross-validation when the same limited data must support both tuning and unbiased estimation. Keep a final untouched set when a consequential claim requires a single confirmatory result.

## Baseline and comparison discipline

Choose a baseline that represents the simplest credible current alternative: prevalence, last value, seasonal naive, business rule, linear model, or shallow tree. Evaluate baseline and candidate on identical eligible rows and metrics. Report absolute result, delta, uncertainty or fold variation, slice behavior, inference cost, and failure modes.

Create a new experiment family if data inclusion, split, target, primary metric, or metric implementation changes. Do not compare scores across incompatible families as if they measured one controlled improvement.

## Falsification checks

- permute labels within valid groups; performance should collapse toward chance;
- remove a suspicious feature family and explain any large drop;
- compare historical snapshot features with current-snapshot features;
- search train and holdout for exact and near duplicates;
- rerun across nearby cutoff dates, seeds, or groups;
- inspect whether threshold choice survives realistic prevalence and capacity;
- reproduce the reported result from a clean environment and frozen inputs.

A failed falsification check invalidates the optimistic interpretation until the path is explained and controlled.
