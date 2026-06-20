# GIS Infrastructure Map

This page develops the geographic layer of the UK Gas & LNG Market Monitor.

The purpose is to understand the UK gas market as a physical network, not just a set of price charts. Gas and LNG prices are shaped by terminals, pipelines, interconnectors, storage sites, shipping routes, weather patterns and geopolitical chokepoints.

## Core question

Where are the key physical points in the UK and European gas system, and how could stress at these locations affect market tightness?

## Why geography matters

Gas markets are spatial systems. A price move in NBP or TTF is often linked to a physical constraint somewhere in the network.

Examples include:

1. LNG cargoes being diverted away from Europe.
2. Low storage levels before winter.
3. Pipeline outages from Norway.
4. Interconnector flows changing between Britain and continental Europe.
5. Shipping risk around chokepoints such as Hormuz, Suez or Bab el-Mandeb.
6. High UK power-sector gas demand during low wind periods.

## Map layers to build

The first version of the map will focus on the following layers.

| Layer | Examples | Why it matters |
|---|---|---|
| UK LNG terminals | South Hook, Isle of Grain, Dragon | Shows where imported LNG enters the UK system |
| Gas interconnectors | BBL, IUK, Moffat | Shows links between Britain, Europe and Ireland |
| Norwegian supply routes | Langeled, Vesterled, FLAGS | Norway is a key source of UK gas supply |
| Storage sites | Rough, Hornsea, Aldbrough, Holford | Storage affects seasonal tightness and winter risk |
| Power demand centres | London, Midlands, North West | Gas burn for power can tighten the system |
| European hubs | TTF, Zeebrugge, Dunkirk | Links UK gas to wider European pricing |
| Chokepoints | Hormuz, Suez, Bab el-Mandeb | LNG route risk and geopolitical exposure |

## First map design

The first prototype should be simple.

- Green markers: supply/import points
- Red markers: demand or consumption zones
- Blue lines: pipelines and interconnectors
- Purple markers: LNG terminals
- Yellow markers: geopolitical or shipping chokepoints

The goal is not to create a perfect infrastructure map immediately. The goal is to create an analyst-style visual that explains how physical flows connect to market risk.

## Data fields

Each infrastructure point should eventually have:

| Field | Meaning |
|---|---|
| name | Name of terminal, pipeline, storage site or hub |
| type | LNG terminal, storage, interconnector, hub, chokepoint |
| country | Country or region |
| latitude | Geographic latitude |
| longitude | Geographic longitude |
| role | What the asset does in the gas system |
| market relevance | Why this point matters for prices or risk |
| source | Where the information came from |

## Example infrastructure table

| Asset | Type | Location | Market relevance |
|---|---|---|---|
| South Hook | LNG terminal | Milford Haven, Wales | Major UK LNG import point |
| Isle of Grain | LNG terminal | Kent, England | Important LNG terminal close to South East demand |
| Dragon LNG | LNG terminal | Milford Haven, Wales | Adds flexibility to UK LNG imports |
| Rough | Storage | North Sea | Historically important UK seasonal storage |
| IUK | Interconnector | UK-Belgium | Links NBP and continental European gas markets |
| BBL | Interconnector | Netherlands-UK | Connects UK with Dutch gas system |
| Moffat | Interconnector | UK-Ireland | Connects GB gas system to Ireland |
| TTF | Gas hub | Netherlands | European benchmark gas price |
| NBP | Gas hub | UK | UK benchmark gas price |

## Analyst interpretation

A GIS map helps answer questions such as:

- Is the UK relying heavily on LNG?
- Are interconnector flows supporting the UK or exporting gas away?
- Is European storage comfortable or stressed?
- Could a chokepoint disruption affect LNG availability?
- Is UK gas tightness being driven by supply, demand, storage or international competition?

## Planned outputs

The final version of this page should include:

1. A static map of UK and European gas infrastructure.
2. An interactive Folium map.
3. A route table for LNG and pipeline flows.
4. Short commentary explaining what the map shows.
5. A link between infrastructure points and the tightness index.

## Current status

This page is at the research design stage.

Next step: create a small CSV of UK gas infrastructure points and use Python/Folium to generate the first interactive map.
