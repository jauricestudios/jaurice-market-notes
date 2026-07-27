# Forecast Error & Volume-at-Risk Model

## Project Summary

This layer extends the energy pricing project by testing volume risk. The Excel pricing model estimates the fixed sale price needed to protect margin. This Python model asks a different question: if demand differs from forecast, how much margin is exposed under different price conditions?

The model uses public NESO demand data and a simple previous-day benchmark forecast. Forecast error is then converted into a volume-at-risk measure and combined with price-stress scenarios to estimate portfolio margin-at-risk.

This is not a full supplier forecasting model. It is a transparent public-data workflow showing how forecast error can become commercial exposure when prices are stressed.

## Business Question

If electricity demand is higher or lower than forecast, how much margin is exposed under normal, extreme and spike-price conditions?

This matters because fixed-price contracts are exposed to both price risk and volume risk. A contract may be priced correctly per MWh, but if actual demand differs from forecast during expensive periods, the supplier or portfolio manager can still face margin pressure.

## Data Used

The model uses public NESO demand data for 2025 and 2026.

The main demand column used is:

`ND`

This is used as the demand measure for the forecast-error model.

The model also uses three price-stress assumptions from the wider pricing project:

| Scenario     |   Price stress |
| ------------ | -------------: |
| Normal case  |  GBP 77.18/MWh |
| Extreme case | GBP 135.71/MWh |
| Spike case   | GBP 696.20/MWh |

These price assumptions are used to translate forecast error into margin-at-risk.

## Forecast Method

The first version uses a simple previous-day benchmark forecast.

For each half-hour settlement period:

`Forecast demand = demand from the same settlement period yesterday`

There are 48 half-hour settlement periods per day, so the model shifts demand by 48 rows.

This is not a sophisticated forecasting method, but it is a useful baseline. It gives a clear benchmark before using more advanced models such as ARIMA, SARIMA, machine learning or weather-adjusted demand forecasting.

## Forecast Error

Forecast error is calculated as:

`Forecast error = actual demand - forecast demand`

The model also calculates absolute forecast error:

`Absolute forecast error = |actual demand - forecast demand|`

The forecast error summary was:

| Metric              |       Value |
| ------------------- | ----------: |
| Mean error          |    -6.63 MW |
| Mean absolute error | 1,927.10 MW |
| P50 absolute error  | 1,351.50 MW |
| P90 absolute error  | 4,420.00 MW |
| P95 absolute error  | 5,850.50 MW |
| P99 absolute error  | 8,674.50 MW |

The mean error is close to zero, which means the previous-day forecast is not strongly biased overall. However, the absolute error measures show that large half-hour demand misses can still occur.

## Volume-at-Risk

The model uses the P95 absolute forecast error as a practical volume-at-risk measure.

At system level:

`P95 absolute forecast error = 5,850.50 MW`

Because each settlement period is half an hour, this is converted into MWh:

`System volume-at-risk = 5,850.50 × 0.5 = 2,925.25 MWh`

This represents the system-level half-hour volume exposure under a large forecast error.

To make the result more realistic for a smaller illustrative portfolio, the model scales the system exposure by 0.1%:

`Portfolio volume-at-risk = 2,925.25 × 0.001 = 2.93 MWh`

## Margin-at-Risk

The portfolio volume-at-risk is then multiplied by each price-stress scenario.

| Scenario     | Portfolio volume-at-risk | Portfolio margin-at-risk |
| ------------ | -----------------------: | -----------------------: |
| Normal case  |                 2.93 MWh |               GBP 225.77 |
| Extreme case |                 2.93 MWh |               GBP 396.99 |
| Spike case   |                 2.93 MWh |             GBP 2,036.56 |

The result shows that the same volume error becomes much more damaging when it occurs during a spike-price period.

## Chart Interpretation

The actual-versus-forecast chart shows that the previous-day benchmark captures the broad shape of demand, but misses some peaks and troughs. These missed movements create volume exposure.

The forecast error distribution is centred close to zero, but the tails show that larger forecast errors can occur. This supports using a high-percentile absolute forecast error as a volume-at-risk measure.

The portfolio margin-at-risk chart shows the commercial effect of applying stressed prices to the same volume-at-risk. The spike case creates a much larger margin impact than the normal and extreme cases.

## Commercial Interpretation

The model shows that volume risk is not only about the size of the forecast error. It also depends on the price environment in which the forecast error occurs.

A portfolio volume-at-risk of 2.93 MWh creates a relatively small margin-at-risk under normal prices. However, under a spike-price case, the same volume exposure creates a much larger margin impact.

This means that energy pricing should not only estimate the required sale price. It should also consider forecast error, volume uncertainty and stressed price conditions.

## Link to Excel Pricing Model

The Excel pricing model answers:

`What fixed sale price is required to protect margin?`

This Python layer answers:

`How much margin remains exposed if demand differs from forecast?`

Together, they create a more complete commercial workflow:

`Price risk + volume risk + scenario analysis + commercial recommendation`

## Limitations

This model uses a simple previous-day forecast rather than a full production-grade demand forecasting model. It does not include weather variables, calendar effects, holidays, customer-specific load shapes, actual hedge positions or live market prices.

The portfolio share is illustrative. A real supplier or customer portfolio would need its own actual demand profile.

The model is therefore best understood as a transparent volume-risk demonstration using public system data, not a full supplier risk engine.

## Next Version

The next version could improve the model by adding:

* Weather variables
* Day-of-week effects
* Holiday flags
* Customer load profiles
* ARIMA or SARIMA forecasting
* Forecast backtesting
* Separate peak and off-peak error analysis
* Integration with the Excel pricing model
* Hedge coverage and imbalance exposure assumptions

The strongest next improvement would be to compare the previous-day benchmark against a better forecasting model and show whether the improved model reduces portfolio margin-at-risk.
