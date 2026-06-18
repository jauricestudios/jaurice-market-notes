# UK Gas Market Forecasting Study

_Last updated: 17 June 2026_

## Research question

Can UK gas market tightness be forecast using historical prices, storage levels, LNG send-out, interconnector flows and weather demand?

## Variables

| Variable | Role in the model |
|---|---|
| NBP gas price | UK gas benchmark |
| TTF gas price | European benchmark |
| NBP minus TTF | UK-Europe pricing pressure |
| Storage level | Physical buffer against demand shocks |
| LNG send-out | Flexible supply entering the system |
| Heating degree days | Weather-driven demand |
| Interconnector flows | Import and export pressure |

## Exploratory analysis

The first stage is visual. The page should include:

- NBP price over time
- TTF price over time
- NBP versus TTF spread
- storage seasonality
- LNG send-out trend
- rolling volatility
- correlation matrix

## Forecasting workflow

The modelling workflow is:

1. clean and align the data
2. create lagged variables
3. split into training and test data
4. build a naive benchmark
5. fit ARIMA or SARIMAX models
6. compare actual and predicted values
7. calculate forecast errors
8. write a commercial interpretation

## Candidate models

| Model | Purpose |
|---|---|
| Naive forecast | Baseline comparison |
| Moving average | Simple smoothing benchmark |
| ARIMA | Univariate time-series forecast |
| SARIMAX | Forecast with storage, weather, LNG and spread variables |
| Scenario forecast | Commercial stress testing |

## Validation

The study should report:

| Metric | Meaning |
|---|---|
| MAE | Average absolute forecast error |
| RMSE | Penalises larger errors |
| MAPE | Percentage forecast error |
| Actual vs predicted chart | Visual model check |
| Residual plot | Checks what the model misses |

## Commercial interpretation

The model should not be treated as a trading signal by itself.

The aim is to understand whether market tightness indicators improve the interpretation of UK gas prices and spreads. A useful model should explain direction, seasonality, volatility and forecast uncertainty, not claim certainty.
