# Reproduction and Handoff Record

## Release identity

- **Project / release:**
- **Version / commit:**
- **Release owner and date:**
- **Status:** reproduced / ready for independent reproduction / replayable with constraints / archival evidence only
- **Independent runner:**
- **Clean-room run ID and date:**
- **Decision supported by this release:**

## Supported scope

- **Question and claims:**
- **Population, unit, and time window:**
- **Authoritative outputs:**
- **Exploratory outputs:**
- **Explicitly unsupported uses:**

## Canonical entry point

```text
COMMAND_FROM_CLEAN_STATE
```

- **Expected runtime / compute / external cost:**
- **Required access and credential owner:**
- **Output and cache locations:**
- **Failure behavior:**

## Artifact and lineage map

| Artifact | Role | Version / hash | Produced by | Upstream IDs | Canonical? | Privacy / retention |
|---|---|---|---|---|---:|---|
|  |  |  |  |  |  |  |

## Input contract

| Input | Snapshot / query identity | Schema / row checks | Access procedure | Mutability risk |
|---|---|---|---|---|
|  |  |  |  |  |

## Environment contract

- **Runtime and lockfile:**
- **OS / container:**
- **Native libraries:**
- **Accelerator / driver:**
- **Locale / timezone:**
- **Required environment variable names:**
- **Seeds and remaining nondeterminism:**

## Acceptance criteria

| Output or invariant | Expected identity / value | Comparison method | Tolerance | Actual | Pass? |
|---|---|---|---|---|---:|
|  |  |  |  |  |  |

## Completion matrix

| Stage | Required? | Evidence / log ID | Independently run? | Result | Constraint or owner |
|---|---:|---|---:|---|---|
| Environment creation |  |  |  |  |  |
| Input acquisition and verification |  |  |  |  |  |
| Preprocessing / features |  |  |  |  |  |
| Model loading or training |  |  |  |  |  |
| Evaluation and independent validation |  |  |  |  |  |
| Final output generation |  |  |  |  |  |
| Expected-output comparison |  |  |  |  |  |

## Human decisions and manual steps

| Date | Actor / role | Decision or edit | Input artifact | Output artifact | Rationale |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Known limitations and rejected approaches

- **Missing or unproven stages:**
- **Data and ground-truth limitations:**
- **Nondeterministic behavior:**
- **Rejected hypotheses / failed experiments that matter:**
- **Evidence that would change the result:**

## Operations and ownership

| Concern | Signal / trigger | Required action | Owner / escalation |
|---|---|---|---|
| Source or schema drift |  |  |  |
| Performance or claim drift |  |  |  |
| Dependency or artifact expiry |  |  |  |
| Retraining / revalidation |  |  |  |
| Retirement |  |  |  |

## Release checks

- [ ] No secrets or credential values
- [ ] No unintended private or personal data
- [ ] No machine-specific absolute paths
- [ ] Canonical artifacts are unambiguous
- [ ] Declared dependencies and licenses are present
- [ ] Public release history was checked for sensitive artifacts
- [ ] Recipient acknowledged constraints and ownership

## Sign-off

| Role | Name | Decision | Date | Conditions |
|---|---|---|---|---|
| Release owner |  |  |  |  |
| Independent runner |  |  |  |  |
| Receiving owner |  |  |  |  |
