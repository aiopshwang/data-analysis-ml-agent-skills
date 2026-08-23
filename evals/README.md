# Skill-selection evaluations

The golden set in trigger-prompts.yaml separates three cases for every skill:

- **direct:** explicitly names the intended workflow;
- **indirect:** describes the failure or goal without naming the skill;
- **negative:** resembles the domain but should not select that skill.

Use the set when editing names or descriptions. Measure selection precision and recall separately, inspect every false positive and false negative, and add a case only when it represents a distinct routing boundary. Do not tune metadata to memorize wording in this file.

Repository tests validate the schema and coverage. Behavioral evaluation still requires running the prompts through a target agent or an independent reviewer.
