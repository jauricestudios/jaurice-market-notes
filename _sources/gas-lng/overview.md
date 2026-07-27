# UK Gas Balance and Physical Optionality

```{admonition} Project focus
:class: note

This project uses public data to study UK and European gas market tightness through flows, storage, LNG send-out, interconnector behaviour, regional spreads and forward curves.
```

## Purpose

This page sets out the structure for a gas market research project focused on physical balance, pricing pressure and flexibility.

The aim is not to build a trading system or claim a proprietary edge. The aim is to show how public data can be organised into a clear market view.

The project focuses on one practical question:

> Is the UK gas market loose or tight, and what does that imply for prices, spreads, storage value and market risk?

By **optionality**, I mean the value created by flexibility. In gas markets, flexibility can come from storage, LNG cargoes, interconnectors, flexible demand or gas-fired generation.

## Why UK gas

UK gas is a useful case study because it connects several parts of the energy system:

- LNG imports
- European pipeline flows
- UK and European storage
- weather-sensitive demand
- gas-fired power generation
- NBP and TTF price spreads
- forward curve structure

This makes it a useful market for studying how physical constraints can move prices.

## Physical market logic

In physical commodity markets, useful signals rarely come from one dataset. A price move only becomes meaningful when it is linked to flows, inventories, infrastructure, timing and demand.

This project uses that logic in a public-data setting.

| Question | What it tests |
|---|---|
| Is the system loose or tight? | Whether supply is comfortable relative to demand |
| Is the forward curve steep or flat? | Whether the market is pricing seasonal scarcity or storage value |
| Is NBP cheap or expensive versus TTF? | Whether UK gas is under pressure relative to continental Europe |
| Are flows behaving normally? | Whether LNG, storage or interconnectors are absorbing stress |
| Where is the flexibility? | Whether storage, LNG or gas-fired generation becomes more valuable |
| What could change the view? | Weather, low wind, outages, shipping disruption or policy shocks |

## Signal interpretation

| Signal | Loose market indication | Tight market indication |
|---|---|---|
| Storage | High and rising storage | Low storage or rapid withdrawals |
| LNG send-out | Strong send-out adding supply | Weak send-out or fewer arrivals |
| Interconnector flows | Imports into the UK or balanced flows | Exports from the UK during domestic tightness |
| Weather demand | Mild conditions | Cold conditions and rising heating demand |
| Gas for power | Low gas burn | High gas burn due to low wind or high residual demand |
| NBP versus TTF | UK discount to continental Europe | UK premium or narrowing discount |
| Forward curve | Flat curve or comfortable summer/winter spread | Winter premium, backwardation or steep seasonal spread |
| Infrastructure | Normal terminal and pipeline availability | Outages, congestion or limited flexibility |

## Data sources

Each dataset should be recorded with its source, frequency, transformation and limitation.

| Data area | Example source | Frequency | Main limitation |
|---|---|---|---|
| Gas prices | ICE, broker snapshots or public market references | Daily or monthly | Live exchange data may require paid access |
| Storage | GIE AGSI, National Gas or official storage publications | Daily or weekly | UK storage is small compared with continental Europe |
| LNG send-out | National Gas, terminal data or public reports | Daily or weekly | Terminal-level data may be incomplete |
| Interconnector flows | National Gas, ENTSOG or operator publications | Daily | Nominations and actual flows may differ |
| Weather demand | Met Office, degree-day proxies or weather datasets | Daily or weekly | Weather is only one demand driver |
| Power data | NESO, Elexon or public power data | Half-hourly, daily or monthly | Raw data often needs cleaning |
| Strategic risk | Government, regulator, company reports and market news | Event-based | Interpretation requires judgement |

## First version outputs

The first version of this project focuses on four outputs.

| Output | Purpose |
|---|---|
| Gas balance table | Summarise supply, demand and net tightness |
| NBP/TTF spread note | Interpret UK gas value relative to continental Europe |
| Forward curve note | Explain seasonal scarcity and storage value |
| Source table | Record sources, assumptions and limitations |

## Analyst update format

Each update should answer six questions:

1. What changed?
2. Which indicator moved?
3. Why does it matter physically?
4. How could it affect prices, spreads or storage value?
5. What is uncertain?
6. What should be watched next?

## Limitations

This is a student research portfolio built from public data. It does not include proprietary trader information such as live bids and offers, private counterparty behaviour, internal inventory data, credit lines, freight negotiations or physical access to terminals and storage.

The purpose is not to claim a trading edge. The purpose is to show a disciplined approach to physical commodity market research using public sources, clear assumptions and honest limitations.

## Next build

The next build will add a simple UK gas balance table and source table. After that, the project will add an NBP/TTF spread chart and a short forward curve interpretation note.
