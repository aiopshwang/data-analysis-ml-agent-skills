# Reproduction Contract

Use this reference when defining what "reproducible" means for a release, designing a clean-room rerun, or auditing a handoff package.

## Choose an honest verification level

| Status | Required evidence |
|---|---|
| Reproduced | An independent clean run completed all material stages and met declared output tolerances |
| Ready for independent reproduction | The package, contracts, and clean entry point are complete, but no independent clean run has been performed yet |
| Replayable with constraints | The workflow and contracts are present, but named stages could not be rerun because access, compute, or external state is unavailable |
| Archival evidence only | Inputs or executable environment cannot be reconstructed; outputs and provenance are retained for inspection |

Do not use "reproduced" for a run in the creator's existing environment, a partial notebook rerun, a successful import, or unit tests alone.

## Define the artifact graph

Every authoritative result should have a directed lineage:

```text
source -> snapshot/query -> cleaned data -> features -> model -> predictions
-> metrics/validation -> report or decision artifact
```

For each node record identity, content hash where possible, creator step, upstream inputs, schema or interface, retention location, and privacy class. For each edge record the command or function, configuration, code revision, environment, and expected output checks.

Human changes - label adjudication, exclusions, threshold approval, spreadsheet correction, narrative editing - are lineage events. Preserve the actor, date, rationale, and before/after artifact identity.

## Specify input reproducibility

Use the strongest available option:

1. immutable source snapshot with checksum;
2. versioned dataset or table partition with durable ID;
3. query plus database snapshot/transaction identity;
4. query plus retrieval time and source version, explicitly acknowledging drift;
5. representative safe fixture for pipeline verification only.

A fixture can prove executable behavior but cannot reproduce population metrics unless it is the evaluated population.

## Specify environment reproducibility

Capture the language/runtime, dependency lock, relevant native libraries, OS/container identity, accelerator and driver when material, locale, timezone, and environment variables by name. Never store secret values. Record credential acquisition and owner separately.

Random seeds are necessary but not sufficient. Identify nondeterministic algorithms, distributed execution order, mutable upstream services, hardware sensitivity, and concurrency. Choose tolerances based on observed repeat-run variance and decision sensitivity.

## Design the clean-room run

The independent runner should receive only the package and documented external access. The acceptance procedure should:

1. verify package and input identities;
2. create the environment from declarations;
3. execute one canonical command from an empty output/cache location;
4. capture logs, timing, and generated manifest;
5. compare every authoritative artifact using declared hashes, tolerances, or invariants;
6. verify that each material claim points to a passing artifact;
7. record every deviation without modifying expected outputs in place.

If expected outputs must change, create a new release and explain why. Do not regenerate the expected value from the candidate run and treat equality as independent proof.

## Match completion evidence to scope

Use a completion matrix rather than one overall checkbox. Evidence must cover each required stage and each declared output. Distinguish:

- static presence: file or declaration exists;
- component execution: one step works;
- integrated execution: connected stages work together;
- end-to-end reproduction: the complete supported path meets acceptance criteria;
- independent reproduction: a separate runner completed that path from a clean state.

Only the last level justifies the strongest status.

## Audit the handoff boundary

The recipient needs to know:

- what decisions the result may and may not support;
- which artifact is canonical and how to verify it;
- how to obtain inputs and credentials;
- expected runtime, compute, storage, and external cost;
- how source or schema drift is detected;
- when retraining, revalidation, or retirement is required;
- who owns data, code, model, validation, and operational decisions;
- what failed approaches or unresolved evidence constrain future changes.

Remove secrets, personal data not essential to the release, machine-specific paths, caches, and accidental large artifacts. Scan both current files and version history when publishing publicly.
