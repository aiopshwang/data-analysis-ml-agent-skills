# Synthetic renewal-risk case

This fictional fixture supports forward testing of the skills. It contains no real customer data.

A customer-success team can contact at most three accounts each Monday. For a review dated 2026-06-01, it wants a model that ranks active accounts by the risk that they will not renew in the following 30 days.

The files came from different internal exports:

- accounts.csv is described as the active-account list;
- activity.csv contains account activity aggregates and lifecycle fields;
- labels.csv contains the billing team's renewal outcome.

The proposed first experiment is a random row split evaluated with accuracy. No formal data contract or label audit has been completed.
