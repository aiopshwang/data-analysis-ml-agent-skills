# Decision-grade project gates

Use these gates for work spanning several data-science lifecycle stages. The gates are evidence checks, not mandatory meetings. Continue without asking when the condition is satisfied and the next action is reversible.

## 1. Decision contract

Pass when a reviewer can answer:

- What decision changes if the result changes?
- Who or what receives one prediction or analytic conclusion?
- What information exists at the decision time?
- What outcome is observed, over what horizon, and how late can it arrive?
- Which error is costly, and what improvement would be useful?

Stop for a material choice when plausible answers define different targets, populations, or acceptable harms. If the work is exploratory, explicitly define the current output as hypothesis generation rather than a validated decision rule.

## 2. Evidence readiness

Pass when source lineage, grain, keys, time semantics, joins, exclusions, and label provenance are supported by checks or authoritative documentation. Record unresolved findings and their affected scope.

Do not pass merely because a file loads or a schema is valid. A technically valid table can still represent the wrong entity, time, or outcome.

## 3. Evaluation lock

Pass before tuning when the following are fixed:

- deployment-matched split and test isolation;
- primary metric, guardrails, and operating threshold if applicable;
- simple baseline and comparison rule;
- minimum worthwhile improvement;
- feature availability cutoff and leakage controls.

If any of these change after results are seen, log the change and treat subsequent evidence as a new experiment family.

## 4. Controlled iteration

Pass a candidate only when its claimed gain is measured against the locked baseline under comparable conditions. Record changed factors, run identifiers, artifacts, variance or uncertainty, slice behavior, compute cost, and failure notes.

Reject complexity that improves only a convenience metric, relies on unavailable features, is unstable across relevant slices, or cannot be reproduced.

## 5. Independent challenge

Before a consequential claim, run a check capable of disproving it: untouched holdout, time backtest, independent record reconciliation, alternative metric, suspicious-feature ablation, negative control, or fresh-run reproduction. The creator's successful rerun is useful but is not independent evidence.

## 6. Decision and handoff

Pass when the final record distinguishes:

- supported findings and their evidence;
- conditions and populations where they apply;
- contradictions, known failure modes, and untested assumptions;
- recommended action and monitoring or rollback trigger;
- exact reproduction path from immutable input to reported artifact.

A dashboard, notebook, or model file alone is not a handoff.

## Status language

Use calibrated labels:

- **supported:** direct evidence passes the prespecified check;
- **conditional:** supported only under explicit constraints;
- **contradicted:** observed evidence conflicts with the claim;
- **not tested:** no adequate check has been run;

Track reproduction independently from claim status: **reproduced**, **ready for independent reproduction**, **replayable with constraints**, **archival evidence only**, or **not assessed**. A claim can be supported by preserved evidence while its computation is not currently reproducible; do not collapse those judgments.
