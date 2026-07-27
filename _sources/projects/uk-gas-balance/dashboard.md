# Gas Market Dashboard

_Last updated: 16 June 2026_


This page is the working dashboard for the UK gas balance project.

The purpose is to bring the main market indicators into one place and use them to judge whether the UK gas market is becoming tighter or looser.

## What the dashboard will show

| Section | Indicator | Why it matters |
|---|---|---|
| Price | NBP gas price | Main UK gas price signal |
| European benchmark | TTF gas price | Main continental European gas benchmark |
| Regional spread | NBP minus TTF | Shows whether the UK is cheap or expensive relative to Europe |
| Storage | UK and EU storage level | Measures buffer against demand shocks |
| LNG | LNG send-out or LNG imports | Shows how much flexible supply is entering the system |
| Interconnectors | UK-Europe gas flows | Shows whether the UK is importing from or exporting to Europe |
| Weather | Heating degree days | Captures weather-driven gas demand |
| Power burn | Gas used for power generation | Links the gas market to the electricity market |
| Market signal | Tightness indicator | Summarises whether conditions look loose, normal or tight |

## Main output

The main output will be a simple dashboard with:

- a gas price chart
- an NBP versus TTF spread chart
- a storage chart
- an LNG send-out chart
- an interconnector flow chart
- a weather demand chart
- a simple market tightness table

## How the dashboard will be used

The dashboard is not meant to predict prices mechanically.

It is meant to support market interpretation. For example, if storage is falling, LNG send-out is weak, temperatures are colder than normal and NBP is rising versus TTF, that would suggest a tighter UK gas market.

If storage is comfortable, LNG send-out is strong, weather demand is mild and NBP is weak versus TTF, that would suggest a looser market.

## Reproducibility

Each chart should be linked to a source table. Each source table should record:

| Field | Meaning |
|---|---|
| Indicator | Name of the variable |
| Source | Where the data came from |
| Frequency | Daily, weekly or monthly |
| Unit | Price, volume, percentage or index |
| Transformation | Spread, moving average, change or normalised value |
| Limitation | Any weakness in the data |

## Next step

The next step is to build the first version using manually collected data, then replace the manual inputs with cleaner Python or Excel workflows.
