# Energy Pricing & Commercial Scenario Model

## Project Summary

This project builds a public-data-informed energy pricing workflow for a fixed-price electricity contract. The aim is to test how wholesale price stress, non-commodity cost assumptions, forecast error and volume uncertainty affect the sale price needed to protect margin.

The project is built in two layers:

1. **Python layer:** uses public NESO demand data to build a simple forecast-error and volume-at-risk model.
2. **Excel layer:** uses cost-stack assumptions, stress scenarios and decision rules to calculate required sale price, margin buffer and commercial recommendation.

The project is not intended to replicate a full supplier pricing engine. It is a transparent portfolio-style model showing how public market data, cost assumptions, scenario analysis and basic risk modelling can support pricing judgement.

## Business Question

What fixed sale price is required to protect margin, and how much margin remains exposed if demand differs from forecast under stressed price conditions?

This matters because energy pricing risk is not only about the price per MWh. It is also about the volume exposed at that price. A contract can be priced sensibly under base assumptions but still become risky if demand is higher than expected during stressed or spike-price periods.

## Project Workflow

The workflow is:

```text
Public NESO demand data
→ Python forecast-error model
→ Volume-at-risk calculation
→ Price-stress margin-at-risk
→ Excel cost-stack pricing model
→ Scenario and sensitivity analysis
→ Commercial recommendation
```

This separates the project into a data layer, a risk layer and a commercial decision layer.

## Python Layer: Forecast Error & Volume-at-Risk

The Python model uses public NESO demand data for 2025 and 2026. The main demand column used is `ND`.

A simple previous-day benchmark forecast is used:

```text
Forecast demand = demand from the same settlement period yesterday
```

Since there are 48 half-hour settlement periods per day, the model shifts demand by 48 rows.

Forecast error is calculated as:

```text
Forecast error = actual demand - forecast demand
```

The model then calculates absolute forecast error and uses the P95 absolute error as a practical volume-at-risk measure.

### Forecast Error Results

| Metric              |       Value |
| ------------------- | ----------: |
| Mean error          |    -6.63 MW |
| Mean absolute error | 1,927.10 MW |
| P50 absolute error  | 1,351.50 MW |
| P90 absolute error  | 4,420.00 MW |
| P95 absolute error  | 5,850.50 MW |
| P99 absolute error  | 8,674.50 MW |

The mean error is close to zero, so the benchmark forecast is not strongly biased overall. However, the high percentile errors show that large demand misses can occur.

## Volume-at-Risk

The P95 system-level forecast error is converted into MWh for a half-hour settlement period:

```text
System volume-at-risk = 5,850.50 MW × 0.5 = 2,925.25 MWh
```

To make this more realistic for an illustrative portfolio, the system exposure is scaled by 0.1%:

```text
Portfolio volume-at-risk = 2,925.25 MWh × 0.001 = 2.93 MWh
```

This avoids overstating the exposure as if a small portfolio were responsible for the whole GB system forecast error.

## Margin-at-Risk

The portfolio volume-at-risk is multiplied by three price-stress cases:

| Scenario     |   Price stress | Portfolio volume-at-risk | Portfolio margin-at-risk |
| ------------ | -------------: | -----------------------: | -----------------------: |
| Normal case  |  GBP 77.18/MWh |                 2.93 MWh |               GBP 225.77 |
| Extreme case | GBP 135.71/MWh |                 2.93 MWh |               GBP 396.99 |
| Spike case   | GBP 696.20/MWh |                 2.93 MWh |             GBP 2,036.56 |

The result shows that the same volume miss becomes much more damaging when it occurs during a spike-price period.

## Excel Layer: Cost-Stack & Breakeven Pricing Model

The Excel workbook estimates the required fixed sale price using a cost-stack approach.

The required sale price is calculated as:

```text
Required Sale Price =
Wholesale Cost
+ Network Cost
+ Policy Cost
+ Balancing Allowance
+ Operating Cost
+ Credit Allowance
+ Risk Premium
+ Target Margin
```

The margin buffer is then calculated as:

```text
Margin Buffer = Offered Sale Price - Required Sale Price
```

A simple decision gate is applied:

| Margin buffer     | Decision |
| ----------------- | -------- |
| Negative          | Reject   |
| Positive but thin | Review   |
| Strong enough     | Accept   |

The workbook includes:

* Main pricing table
* Scenario design
* Sensitivity table
* Model checks
* Cost-stack chart
* Required sale price chart
* Commercial recommendation
* Limitations box
* Source register

## Scenario Design

The Excel model tests five pricing scenarios:

1. Base case
2. Wholesale stress
3. Non-commodity stress
4. Combined stress
5. Defensive pricing

The base case represents normal pricing assumptions. Wholesale stress increases the main energy cost. Non-commodity stress increases cost allowances such as network, policy and balancing costs. Combined stress tests several cost pressures at once. Defensive pricing adds a larger risk premium and target margin.

## Commercial Interpretation

The Excel model shows the required sale price needed to protect margin under each pricing scenario. The Python layer shows how forecast error can create remaining margin exposure even after a price has been set.

Together, the project shows that fixed-price energy contracts need both:

```text
Price-risk analysis
and
Volume-risk analysis
```

The main commercial message is:

```text
A fixed sale price should not be judged only against base wholesale cost. It should be tested against the full cost stack, stressed price conditions and forecast-volume uncertainty.
```

## Key Outputs

The project produces:

```text
forecast_error_summary.csv
volume_at_risk_summary.csv
demand_forecast_error_model.csv
actual_vs_forecast_demand.png
forecast_error_distribution.png
portfolio_margin_at_risk_by_scenario.png
energy_cost_stack_breakeven_model.xlsx
```

## Limitations

This project uses public data and simplified assumptions. It does not include:

* Real customer load profiles
* Live forward curves
* Actual hedge books
* Supplier tariff structures
* Collateral requirements
* Detailed network charging methodology
* Weather-adjusted demand forecasting
* Customer-level imbalance exposure

The portfolio share is illustrative. A real supplier or customer portfolio would need its own actual load profile and risk limits.

## Next Version

The next version could improve the model by adding:

* Weather variables
* Day-of-week effects
* Holiday effects
* Customer load profiles
* ARIMA or SARIMA forecasting
* Forecast backtesting
* Peak and off-peak forecast-error analysis
* Power Query or Python-linked Excel inputs
* Hedge coverage assumptions
* Live price or forward curve inputs

The strongest next improvement would be to compare the previous-day benchmark against a more advanced forecasting model and test whether improved forecasting reduces portfolio margin-at-risk.

## Skills Demonstrated

This project demonstrates:

* Python data cleaning
* Forecast-error analysis
* Volume-at-risk calculation
* Public market data use
* Excel cost-stack modelling
* Scenario and sensitivity analysis
* Commercial recommendation writing
* Source register and model limitation documentation
