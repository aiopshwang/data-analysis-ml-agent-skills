# ML Failure Investigation Log

## Incident identity

- **Incident / issue ID:**
- **Owner:**
- **Opened / updated:**
- **Impact and affected decision:**
- **Current status:** investigating / mitigated / root cause verified / unresolved
- **First known bad:**
- **Last known good:**

## Reproducible symptom

- **Expected behavior:**
- **Observed behavior:**
- **Affected population and grain:**
- **Unaffected control:**
- **Reproduction entry point:**
- **Frequency:**
- **Input, code, config, artifact, and environment IDs:**
- **Smallest failing case or paired comparison:**

## Change inventory

| Dimension | Last known good | First known bad | Confirmed difference? |
|---|---|---|---:|
| Source snapshot / query |  |  |  |
| Code revision |  |  |  |
| Configuration |  |  |  |
| Model artifact |  |  |  |
| Dependencies / runtime |  |  |  |
| Metric / threshold |  |  |  |

## Boundary trace

| Layer | Invariant or record field | Expected / good | Observed / bad | Evidence ID | First divergence? |
|---|---|---|---|---|---:|
| Source and semantics |  |  |  |  |  |
| Ground truth |  |  |  |  |  |
| Split and sampling |  |  |  |  |  |
| Feature pipeline |  |  |  |  |  |
| Model artifact |  |  |  |  |  |
| Metric / decision logic |  |  |  |  |  |
| Runtime / delivery |  |  |  |  |  |

## Hypothesis ledger

| ID | Hypothesis | Prediction if true | Discriminating test | Result / evidence | Status | Reopen condition |
|---|---|---|---|---|---|---|
| H-01 |  |  |  |  | open |  |

Allowed status: `open`, `supported`, `rejected`, `blocked`.

## Experiment log

| Time | Experiment | Single intended change | Control | Result | Interpretation | Artifact / log ID |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## Human ground-truth review

- **Why review was required:**
- **Prespecified sampling method:**
- **Reviewer independence and blinding:**
- **Original label / reviewer decision / adjudicated label locations:**
- **Disagreement and ambiguity:**
- **Population-level inference supported by the sample:**

## Root-cause closure

- **First broken layer:**
- **Causal factor:**
- **Mechanism connecting cause to symptom:**
- **Controlled intervention:**
- **Recovery evidence:**
- **Unaffected control evidence:**
- **Scope matched to the original failure:** yes / no - explain
- **Root cause, mitigation only, or unresolved:**

## Fix and regression coverage

| Original failure scope | Fix | Regression check | Negative control | Result | Owner |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Rejected hypotheses worth preserving

Summarize strong negative findings that future investigators should not repeat without new evidence.

## Remaining risk and next action

- **Unresolved hypotheses:**
- **Known blind spots:**
- **Monitoring signal:**
- **Next discriminating test, owner, and due date:**
