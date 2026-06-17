# Data and Methodology

_Last updated: 16 June 2026_


This page records the data sources, transformations and limitations used in the UK gas balance project.

## Data discipline

Every dataset should have a clear source, frequency, unit and limitation. This matters because market analysis is only useful if the reader can see where the numbers came from.

## Source table template

| Data area | Example indicator | Source type | Frequency | Limitation |
|---|---|---|---|---|
| Price | NBP gas price | Market price provider or public snapshot | Daily | Public data may be delayed or incomplete |
| Price | TTF gas price | Market price provider or public snapshot | Daily | Contract choice must be stated |
| Storage | Storage level | GIE or national storage publication | Daily or weekly | UK storage is smaller than continental storage |
| LNG | LNG send-out | National Grid, terminal data or public reports | Daily or weekly | Terminal level data may be incomplete |
| Interconnectors | UK-Europe gas flows | ENTSOG, National Grid or operator data | Daily | Flow direction can change quickly |
| Weather | Heating degree days | Met Office or weather datasets | Daily | Weather stations may not represent all demand areas |
| Power | Gas generation | NESO, Elexon or grid data | Half-hourly or daily | Needs aggregation before analysis |

## Transformation rules

| Transformation | Use |
|---|---|
| NBP minus TTF | Measures UK price premium or discount versus Europe |
| 7-day moving average | Smooths noisy daily data |
| Year-on-year comparison | Compares current conditions with the same season |
| Normalised score | Converts different indicators into one tightness index |
| Red amber green signal | Gives a simple market interpretation |

## Method

The project should move from raw data to interpretation in this order:

1. collect data
2. clean the data
3. record source and frequency
4. transform indicators
5. build charts and tables
6. interpret the signal
7. write a short analyst note

## Limitation

The dashboard should not pretend to be a trading model. It is a structured market research tool. The aim is to show evidence, not to claim certainty.
