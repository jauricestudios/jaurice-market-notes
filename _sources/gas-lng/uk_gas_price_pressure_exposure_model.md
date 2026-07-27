# UK Gas Price Pressure and Exposure Model

This project builds a Python gas-market pipeline that combines UK physical gas-system indicators, European gas benchmarks and global LNG pricing, then converts those signals into a commercial cost exposure model for a UK gas-exposed buyer.

## Project question

How can physical gas-system pressure, traded gas benchmarks and global LNG context be combined into a commercial exposure model for a UK gas-exposed buyer?

## Business case

The model considers a UK medium-sized food manufacturer using 10,000 MWh of gas per month.

The buyer is assumed to have 60% hedge cover, leaving 4,000 MWh exposed to floating gas prices.

The model uses NBP as the main UK gas benchmark and tests how different market stress scenarios affect monthly gas cost.

## Python workflow

The Python pipeline covers four layers:

1. UK physical gas pressure using weather, wind and storage indicators.
2. Price response testing using SAP, NBP and TTF.
3. Global gas benchmark comparison using NBP, TTF and JKM in £/MWh.
4. Commercial buyer exposure modelling using hedge cover and unhedged volume.

## Key result

The physical Gas Tightness Index is useful as a local pressure indicator, but traded gas benchmarks explain short-term price movement more strongly.

NBP and TTF are closely linked European benchmarks, while JKM adds global LNG context.

## Commercial exposure model

The final layer converts market shocks into buyer cost impact.

Under the European TTF stress case, the estimated monthly commodity cost impact is about £20.8k for a buyer with 60% hedge cover.

If the buyer had no hedge cover, the same scenario would create an estimated monthly cost impact of about £52k.

## Commercial exposure by scenario

![Commercial exposure by scenario](images/commercial_exposure_cost_impact_by_scenario.png)

## Hedge sensitivity

![Hedge sensitivity](images/hedge_sensitivity_cost_impact.png)

## Global gas benchmarks

![Global gas benchmarks](images/global_gas_prices_gbp_2021_2026.png)

## NBP-TTF spread

![NBP-TTF spread](images/barchart_nbp_ttf_spread_gbp_2021_2026.png)

## Limitations

This is a scenario model, not a price forecast.

The scenario shocks are transparent assumptions rather than estimated future prices.

Raw vendor data is not published. The project keeps the code, charts, summary outputs and source documentation visible, while raw market downloads remain excluded.

## Project repository

The full project code and outputs are stored in the separate `energy_pricing_model` repository.
