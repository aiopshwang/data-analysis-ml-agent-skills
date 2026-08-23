# Evaluation strategy

This project evaluates two different questions.

## Selection quality

Does an agent select the right skill for a user's request?

The golden prompt set includes direct requests, indirect descriptions, and close negative cases for every skill. Metadata changes should improve recall without causing unrelated data or software tasks to trigger the suite.

Measure:

- recall on direct and indirect positive prompts;
- precision against negative and neighboring-skill prompts;
- confusion between lifecycle orchestration and narrow specialist skills;
- description length and discovery cost.

## Behavioral quality

Does loading the skill improve the work?

Forward tests should use realistic, unseen tasks and inspect observable artifacts. Useful checks include:

- decision, grain, target, and time boundary are explicit before modeling;
- raw inputs are preserved and transformations have lineage;
- label and ground-truth assumptions are examined;
- leakage-safe splits and a simple baseline are defined;
- material claims map to scope-matched evidence;
- failed hypotheses and unresolved evidence stay visible;
- the final package states exactly what was and was not reproduced.

Use an independent evaluator when practical. Do not provide the intended answer or suspected failure to that evaluator.

## Release gate

A release requires:

1. all skill and plugin validators pass;
2. all local links resolve;
3. the public-content scan passes, including an external private-term denylist before publication;
4. trigger cases cover every skill;
5. representative independent forward tests find no critical workflow regression;
6. the installation source and release tag resolve from the public repository.

Static validation is necessary but does not by itself prove decision quality.

The first public evidence record is the [v0.1.0 independent forward test](https://github.com/aiopshwang/data-analysis-ml-agent-skills/blob/main/evals/results/v0.1.0-forward-test.md).
