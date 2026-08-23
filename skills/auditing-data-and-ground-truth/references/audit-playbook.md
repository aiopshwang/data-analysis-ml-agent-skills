# Data and ground-truth audit playbook

Select checks according to the intended decision and failure risk. Do not run a large catalog without explaining what each check can falsify.

## Grain and identity

- Compare total rows, distinct candidate keys, and distinct real-world entities.
- Test key uniqueness within the time or source boundaries where uniqueness is claimed.
- Sample duplicates and classify exact replay, legitimate repeated event, correction, or unresolved collision.
- Check whether aggregations change the target population or create unequal observation periods.

High-risk signal: the modeled row does not map one-to-one to the decision unit.

## Joins and coverage

For each join, record expected cardinality and measure:

- unmatched keys on both sides;
- duplicate keys per side;
- row counts before and after;
- entity counts before and after;
- multiplication-factor distribution;
- whether missing matches cluster by source, time, or outcome.

High-risk signal: join survival or multiplication depends on the target or a protected or operationally important slice.

## Missingness and encoded absence

Separate unavailable, not applicable, not collected, failed extraction, suppressed, and true zero. Compare missingness by source, time, target, and population slice. Inspect sentinel values and default-filled fields before converting types.

High-risk signal: missingness is downstream of the outcome or a processing path unavailable in production.

## Time and historical truth

Distinguish:

- event time: when reality occurred;
- effective time: when a value became valid;
- record time: when the system stored it;
- availability time: when the model or analyst could retrieve it;
- update time: when a correction or backfill occurred.

Check negative durations, impossible sequences, time-zone changes, late arrivals, backfills, snapshot reconstruction, and use of current attributes for historical cases.

High-risk signal: a historically evaluated row contains a corrected or enriched value that was unavailable then.

## Ground-truth provenance

Trace label construction as a chain:

`real-world event -> source record -> extraction -> rule or annotation -> adjudication -> encoded label`

At each link, identify owner, timestamp, version, exclusions, and failure behavior. Measure coverage and unresolved labels. For human labels, measure agreement on a shared sample and examine disagreements by class and slice; agreement alone does not establish correctness. For delayed outcomes, establish a maturity cutoff and treat immature examples separately.

High-risk signals include using treatment or follow-up as proof of the original condition, treating missing follow-up as a negative, circularly validating a label against a derivative of itself, and allowing unresolved cases into a forced binary target.

## Independent reconciliation

Within the authorized access boundary, choose samples that can reveal systematic failure: random, edge cases, positives, negatives, missing labels, high-loss cases, and relevant sources or time periods. Compare against an approved operational record, original document, or independent reviewer that does not inherit the same transformation path. If that evidence requires new access or external sharing, specify the needed reconciliation and obtain authority before retrieving or transmitting records.

Record the sampling method, reviewer, evidence accessed, mismatch taxonomy, and estimated affected scope. Keep examples privacy-safe in public artifacts.

## Severity and readiness

Classify a finding by consequence, not cosmetic size:

- **critical:** can reverse the target, split, metric, or primary conclusion;
- **major:** materially biases a population, time period, or operational slice;
- **moderate:** limits interpretation or reproducibility but has a bounded workaround;
- **minor:** does not change the conclusion and is straightforward to correct.

An unresolved critical or major finding normally means `not ready` or `unknown`. A condition is acceptable only when it is explicit, enforced, and reflected in the claimed scope.
