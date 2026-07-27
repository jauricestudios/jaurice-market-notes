# Insurance Pricing Model

_Last updated: 17 June 2026_

This page will contain an insurance-style pricing project.

The aim is to show how pricing can be built from exposure, claims, rating factors, loss ratios and model validation.

## Main question

How can policy, exposure and claims data be used to estimate a fair technical premium?

## Data structure

| Data field | Meaning |
|---|---|
| Policy ID | Unique policy reference |
| Exposure | Time at risk |
| Premium | Amount charged |
| Claim count | Number of claims |
| Claim cost | Total cost of claims |
| Region | Location factor |
| Age band | Customer or asset age group |
| Product type | Type of policy |
| Channel | Broker, direct or online |
| Renewal flag | New business or renewal |

## Pricing workflow

1. clean policy and claims data
2. calculate exposure
3. calculate claim frequency
4. calculate claim severity
5. calculate loss ratio
6. test rating factors
7. fit a GLM-style pricing model
8. compare predicted and actual claims cost
9. produce premium indication
10. explain limitations

## Outputs

- claims frequency table
- severity table
- loss ratio chart
- rating factor analysis
- actual versus predicted chart
- premium indication table
- model validation summary
- pricing recommendation

## Tools

- Excel for summaries, PivotTables and pricing tables
- SQL for joining policy and claims data
- Python or R for GLM modelling and validation
- Power BI or Excel dashboard for reporting

## Why this matters

Insurance pricing is not only about building a model. It is about turning messy claims and exposure data into a price that is technically reasonable, commercially usable and explainable.
