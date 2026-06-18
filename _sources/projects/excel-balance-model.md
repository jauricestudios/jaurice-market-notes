# Pricing & Scenario Model

_Last updated: 17 June 2026_

This page documents the Excel version of the commercial pricing and scenario model.

The aim is to build a workbook that can take market data, costs, assumptions and scenarios, then produce pricing outputs, margin checks and dashboard summaries.

## Workbook structure

| Sheet | Purpose |
|---|---|
| Control Panel | Dates, assumptions and scenario settings |
| Sources | Data source list and update notes |
| Raw Data | Imported or pasted market data |
| Clean Data | Standardised dates, units and checks |
| Pricing Model | Price, spread, cost or margin calculation |
| Scenarios | Base, upside and downside assumptions |
| Sensitivities | Data tables for key assumptions |
| Risk Output | Price shock, margin and exposure checks |
| Dashboard | Charts and summary outputs |

## Excel tools used

| Tool | Use |
|---|---|
| XLOOKUP | Pull matching values from source tables |
| INDEX MATCH | Alternative lookup method |
| PivotTables | Summarise data by month, product or region |
| Power Query | Import and clean repeatable data |
| LET | Make long formulas easier to read |
| LAMBDA | Create reusable pricing or cost formulas |
| Data validation | Control scenario inputs |
| Conditional formatting | Highlight high-risk or low-margin cases |
| Data tables | Run sensitivity analysis |
| VBA | Refresh data, clear outputs or export charts |

## Possible applications

| Area | Example use |
|---|---|
| Energy | Gas spread and storage scenario model |
| Insurance | Premium indication and loss ratio dashboard |
| Logistics | Delivered cost and route comparison |
| Supply chain | Supplier cost and margin model |
| Investment | NPV and sensitivity model |
| Risk | Price shock and exposure model |

## Outputs

- pricing table
- scenario dashboard
- sensitivity table
- margin check
- risk flag
- source and assumption table
- written commercial interpretation
