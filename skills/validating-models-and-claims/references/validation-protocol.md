# Validation Protocol

Use this reference when designing or reviewing a formal validation, especially when claims depend on human labels, untouched data, subgroup behavior, or operational equivalence.

## 1. Convert prose into testable claims

A claim is reviewable only when these fields are fixed:

| Field | Question |
|---|---|
| Outcome | What observable result is predicted? |
| Population | For whom or what does it apply? |
| Unit | Is evaluation per event, entity, session, day, or another grain? |
| Horizon | At what prediction and observation times? |
| Comparator | Better than what current method or baseline? |
| Threshold | What practical change counts as success? |
| Conditions | Under which data, workflow, and operating constraints? |
| Decision | What action changes if the claim is supported? |

Split compound claims. "Accurate and robust enough to deploy" contains at least predictive, robustness, operational, and decision-value claims requiring different evidence.

## 2. Match proof to scope

Use the strongest status all evidence permits:

- **Supported:** direct, valid evidence covers the stated scope and meets predefined criteria.
- **Partially supported:** evidence covers only a stated subset or meets only some criteria.
- **Unsupported:** valid evidence contradicts the claim or misses its acceptance criterion.
- **Not tested:** no valid evidence covers the claim.

Common invalid substitutions:

| Claimed scope | Insufficient evidence |
|---|---|
| Future cohorts | Random split of the same historical cohort |
| New entities | Rows from the same entities in train and test |
| End-to-end workflow | Unit tests of the model function |
| Subgroup reliability | Overall metric only |
| Business improvement | Offline discrimination metric only |
| Ground-truth accuracy | Agreement with one unreviewed label source |
| Stable operation | One successful execution |

## 3. Establish independent validation

Record independence along four axes:

1. **Data:** Was the set untouched during feature, model, threshold, and policy selection?
2. **People:** Did validators avoid constructing the artifact or claimed result?
3. **Procedure:** Was the protocol frozen before results were observed?
4. **Execution:** Was the final artifact run through a clean entry point with production-equivalent preprocessing?

Perfect independence is not always feasible. State compromises and the bias they may introduce. If evaluation results cause any model or threshold change, that set becomes development evidence; reserve or obtain new validation evidence for the changed artifact.

## 4. Review human ground truth

For judgment-dependent targets, capture:

- the case sampling frame, including hard negatives and ambiguous cases;
- reviewer qualifications and written instructions;
- whether reviewers were blinded to predictions and prior labels;
- per-reviewer decisions before consensus;
- raw agreement and chance-adjusted agreement where appropriate;
- adjudication rules and the adjudicator's independence;
- unresolved or inherently ambiguous cases;
- label version and effective date.

Do not collapse disagreement into a single label without preserving it. Consider evaluating against a distribution of reviewer judgments or reporting performance separately for high-consensus and ambiguous cases.

## 5. Analyze performance without hiding uncertainty

Select metrics from decision costs and prevalence, not convention. Report the denominator and aggregation unit. Add confidence intervals or resampling intervals appropriate to the data-generating structure; clustered observations require entity- or group-aware resampling.

At minimum compare:

- the declared baseline or current process;
- the locked candidate at the intended operating threshold;
- meaningful temporal, demographic, operational, and data-quality slices;
- high-cost errors and an unbiased error sample;
- calibration or decision consequences when scores drive action.

Treat slice analysis as exploratory unless hypotheses and multiplicity handling were predefined. Small slices should show counts and uncertainty rather than confident rankings.

## 6. Verify operational equivalence

Check that validation inputs exist at decision time and follow the deployed transformation path. Confirm feature order, defaults, artifact version, class mapping, threshold, abstention policy, and output postprocessing. A copied offline pipeline is not evidence of equivalence; compare representative records across the boundary.

## 7. Calibrate the final language

Prefer precise conclusions:

- "On the untouched March-May cohort, the locked model improved recall at the fixed false-positive budget."
- "Evidence is insufficient for new regions because none were represented in independent validation."
- "The result is exploratory because the threshold was selected after inspecting this cohort."

Avoid "validated," "production-ready," "generalizes," or "safe" without specifying the evidence and scope that justify the term.
