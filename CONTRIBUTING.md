# Contributing

Contributions are welcome when they make a real data-analysis or machine-learning decision more reliable without turning the skills into a generic checklist.

## Before proposing a change

Open an issue for a new skill or a material workflow change. Explain:

- the user goal and failure mode;
- why an existing skill cannot handle it;
- the observable behavior that should change;
- how the change can be tested with direct, indirect, and negative prompts.

Small corrections, clearer examples, and portability fixes can go directly to a pull request.

## Development

1. Create a virtual environment.
2. Install `requirements-dev.txt`.
3. Run `python scripts/validate_repo.py`.
4. Run `pytest`.

Keep each skill focused on one recognizable goal. Put conditional detail in `references/`, output templates in `assets/`, and keep `SKILL.md` concise. Never commit customer data, private paths, credentials, proprietary labels, or examples copied from confidential work.

## Pull-request evidence

Describe the problem, the change, the test prompts, and the observed outcome. Record rejected approaches when they materially explain the final design. A green syntax check alone is not proof that an agent behaves better.
