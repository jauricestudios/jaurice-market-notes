# Energy Pricing & Commercial Scenario Model

## Project Summary

This project builds a public-data-informed energy pricing workflow for a fixed-price electricity contract. The aim is to test how wholesale price stress, non-commodity cost assumptions, forecast error and volume uncertainty affect the sale price needed to protect margin.

The project combines two layers:

- a Python forecast-error and volume-at-risk model using public NESO demand data
- an Excel cost-stack and breakeven pricing model for commercial scenario analysis

The model is not intended to replicate a full supplier pricing engine. It is a transparent portfolio project showing how public data, simplified assumptions and scenario analysis can support pricing judgement.

## Business Question

What fixed sale price is required to protect margin, and how much margin remains exposed if demand differs from forecast under stressed price conditions?

Energy pricing risk is not only about the price per MWh. It is also about the volume exposed at that price. A contract can look acceptable under base assumptions but become risky if demand is higher than expected during expensive periods.

## Workflow

Public NESO demand data  
→ Python forecast-error model  
→ Volume-at-risk calculation  
→ Price-stress margin-at-risk  
→ Excel cost-stack pricing model  
→ Scenario and sensitivity analysis  
→ Commercial recommendation  

## Python Layer: Forecast Error and Volume-at-Risk

The Python model uses public NESO demand data for 2025 and 2026. A simple previous-day benchmark forecast is used:

**Forecast demand = demand from the same settlement period yesterday**

There are 48 half-hour settlement periods per day, so the model shifts demand by 48 rows.

Forecast error is calculated as:

**Forecast error = actual demand - forecast demand**

The model then uses the P95 absolute forecast error as a practical volume-at-risk measure.

## Forecast Error Results

| Metric | Value |
|---|---:|
| Mean error | -6.63 MW |
| Mean absolute error | 1,927.10 MW |
| P50 absolute error | 1,351.50 MW |
| P90 absolute error | 4,420.00 MW |
| P95 absolute error | 5,850.50 MW |
| P99 absolute error | 8,674.50 MW |

The mean error is close to zero, so the previous-day forecast is not strongly biased overall. However, the high percentile errors show that large demand misses can occur.

## Actual vs Forecast Demand

![Actual versus previous-day forecast demand](../energy_pricing_model/charts/actual_vs_forecast_demand.png)

The previous-day benchmark captures the broad daily demand shape, but it misses some peaks and troughs. These missed movements create volume exposure.

## Forecast Error Distribution

![Forecast error distribution](../energy_pricing_model/charts/forecast_error_distribution.png)

The error distribution is centred close to zero, but the tails show that larger forecast errors can occur. This supports using a high-percentile absolute forecast error as a volume-at-risk measure.

## Volume-at-Risk

The P95 absolute forecast error is **5,850.50 MW**.

Because each settlement period is half an hour, this is converted into MWh:

**System volume-at-risk = 5,850.50 × 0.5 = 2,925.25 MWh**

To avoid overstating the exposure, the model scales this by an illustrative 0.1% portfolio share:

**Portfolio volume-at-risk = 2,925.25 × 0.001 = 2.93 MWh**

## Margin-at-Risk

| Scenario | Price stress | Portfolio volume-at-risk | Portfolio margin-at-risk |
|---|---:|---:|---:|
| Normal case | GBP 77.18/MWh | 2.93 MWh | GBP 225.77 |
| Extreme case | GBP 135.71/MWh | 2.93 MWh | GBP 396.99 |
| Spike case | GBP 696.20/MWh | 2.93 MWh | GBP 2,036.56 |

![Portfolio margin at risk by price scenario](../energy_pricing_model/charts/portfolio_margin_at_risk_by_scenario.png)

The same volume miss becomes much more damaging when it occurs during a spike-price period.

## Excel Layer: Cost-Stack and Breakeven Pricing

The Excel workbook estimates the fixed sale price needed to cover the full cost stack and target margin.

The required sale price is calculated as:

**Required Sale Price = Wholesale Cost + Network Cost + Policy Cost + Balancing Allowance + Operating Cost + Credit Allowance + Risk Premium + Target Margin**

The margin buffer is calculated as:

**Margin Buffer = Offered Sale Price - Required Sale Price**

The workbook tests base, wholesale stress, non-commodity stress, combined stress and defensive pricing scenarios.

## Commercial Interpretation

The Excel layer answers: **What price should be charged?**

The Python layer answers: **How much margin remains exposed if demand differs from forecast?**

Together, the project shows that fixed-price energy contracts should be tested against both price risk and volume risk.

The main commercial conclusion is that a fixed sale price should not be judged only against base wholesale cost. It should be tested against the full cost stack, stressed price conditions and forecast-volume uncertainty.

## Limitations

This project uses public data and simplified assumptions. It does not include real customer load profiles, live forward curves, actual hedge books, supplier tariff structures, collateral requirements, detailed network charging methodology or weather-adjusted demand forecasting.

The portfolio share is illustrative. A real supplier or customer portfolio would need its own actual load profile and risk limits.

## Files

Main project files:

- `energy_pricing_model/README.md`
- `energy_pricing_model/scripts/forecast_error_volume_risk.py`
- `energy_pricing_model/excel/energy_cost_stack_breakeven_model.xlsx`
- `energy_pricing_model/outputs/forecast_error_summary.csv`
- `energy_pricing_model/outputs/volume_at_risk_summary.csv`

## Skills Demonstrated

- Python data cleaning
- Forecast-error analysis
- Volume-at-risk calculation
- Public energy-market data use
- Excel cost-stack modelling
- Scenario and sensitivity analysis
- Commercial recommendation writing
- Model limitation documentation
