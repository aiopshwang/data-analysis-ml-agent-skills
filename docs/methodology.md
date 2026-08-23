# Decision-Grade Data Science methodology

Decision-grade work is analysis or modeling whose evidence is strong enough for the stated decision and whose limitations remain visible. It does not mean every project needs a heavyweight governance process.

## The evidence chain

Each material conclusion should remain traceable through:

    decision
      → target or analytical claim
      → population, grain, and time boundary
      → source and ground truth
      → evaluation contract
      → experiment and artifact
      → independent challenge
      → supported wording
      → reproduction and owner

A break in this chain narrows the claim. It should not be filled by confidence, a polished chart, or a model's agreement with its own prior output.

## Human-controlled autonomy

The agent should continue through ordinary, reversible work without turning every detail into a meeting. Human approval is reserved for material choices such as changing the source of truth, target, evaluation population, error tradeoff, irreversible data treatment, material spend, or external publication.

Approval establishes authority; it does not establish correctness. The decision and its evidence still belong in the record.

## Evidence-gated complexity

Start with the cheapest credible baseline. Add complexity only when a measured failure identifies what the change is expected to improve. Compare under the same data, split, metric, and budget, and retain negative results.

This rule applies to model families, LLM calls, feature pipelines, retrieval layers, ensembles, and infrastructure. Complexity without a falsifiable purpose is deferred.

## Ground truth and independence

Labels, benchmarks, and existing reports are evidence sources, not unquestionable truth. Audit their provenance, definitions, observation timing, exclusions, and disagreement. Judgment-dependent labels require preserved reviewer decisions and human adjudication.

Whenever consequences are material, challenge a claim with evidence that did not create it: an untouched cohort, independent record reconciliation, blind review, negative control, suspicious-feature ablation, alternate metric, or clean-room rerun.

## Calibrated completion

Completion is proven at the scope of the claim. A component test cannot prove an end-to-end workflow; one corrected example cannot prove a population regression is fixed; a creator's rerun is not independent reproduction.

Final language distinguishes supported, conditional, contradicted, and not-tested claims. Missing evidence remains missing rather than becoming an implicit pass.

## Portability

The skills intentionally avoid fixed model vendors, sample-size thresholds, metrics, and statistical methods. Those choices depend on the decision, data-generating process, error costs, and operating environment.
