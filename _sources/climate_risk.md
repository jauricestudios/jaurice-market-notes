# Climate Exposure Risk Map: UK Energy Infrastructure Prototype

This project builds a geospatial exposure-screening workflow for operational UK renewable energy infrastructure.

The aim is to show how public infrastructure data can be cleaned, mapped, scored and interpreted for physical climate risk, insurance, infrastructure and portfolio risk use cases.

This is not a production catastrophe model. It is a transparent Version 1 screening model that demonstrates the workflow from raw asset data to regional and asset-level exposure summaries.

---

## Project question

Where might physical climate exposure be concentrated across UK renewable energy infrastructure?

More specifically:

> Which operational renewable energy assets may warrant closer review under a first-pass physical climate exposure screening framework?

---

## Why this project matters

Physical climate risk analysis depends on knowing where assets are located, what type of assets they are, how large or important they may be, and how exposure varies across regions.

This project starts with a messy public infrastructure dataset and turns it into a structured geospatial asset layer that can support exposure analysis.

The workflow is relevant to infrastructure risk analysis, insurance exposure management, portfolio screening, energy system resilience, economic research and geospatial data science.

---

## Data source

The project uses the Renewable Energy Planning Database, Q4 2025 extract.

The raw dataset contains:

- 13,995 project records
- 53 original fields

The cleaned modelling dataset contains:

- 3,060 operational assets before coordinate filtering
- 3,058 operational assets with valid coordinates

Two operational records were removed because they were missing coordinate values.

---

## Methodology

### 1. Data cleaning

The raw dataset was reduced to the fields needed to identify, describe and locate assets.

Key fields included:

- site name
- operator or applicant
- technology type
- installed capacity
- development status
- region
- country
- X-coordinate
- Y-coordinate

The `Development Status` field was cleaned before filtering because real-world datasets often contain inconsistent spelling, capitalisation or hidden whitespace.

The first modelling decision was to focus on operational assets only.

---

### 2. Geospatial asset layer

The cleaned operational asset table was converted into a GeoDataFrame using GeoPandas.

The asset coordinates use British National Grid coordinates, so the coordinate reference system was set to `EPSG:27700`.

This matters because distance-based geospatial analysis depends on using the correct coordinate system.

Each asset was converted into a point geometry, creating a reusable spatial asset layer.

---

### 3. Exposure proxy features

A first-pass geographic exposure proxy was created using distance to a boundary proxy.

This feature is not a formal climate hazard layer. It is a prototype feature used to demonstrate the exposure-screening workflow.

In a stronger version of the project, this proxy would be replaced with formal hazard data such as flood zones, heat stress layers, coastal erosion data, climate scenario rasters or infrastructure vulnerability data.

---

### 4. Preliminary exposure scoring

The preliminary score combines:

- proximity score
- installed-capacity score

Installed capacity is used as a simple proxy for asset scale. It is not the same as insured value, replacement cost, revenue exposure or criticality.

The final score is converted into Low, Medium and High screening categories.

These categories are prioritisation labels only. They are not validated catastrophe risk bands.

---

## Example code

### Cleaning the development status field

```python
assets["development_status_clean"] = (
    assets["Development Status"]
    .astype(str)
    .str.strip()
    .str.lower()
)

operational_assets = assets[
    assets["development_status_clean"] == "operational"
].copy()
cat >> climate_risk.md <<'EOF'
```

This standardises the status field before filtering so that hidden whitespace or inconsistent capitalisation does not exclude valid operational assets.

### Creating the spatial asset layer

```python
assets_gdf_27700 = gpd.GeoDataFrame(
    assets,
    geometry=gpd.points_from_xy(
        assets["X-coordinate"],
        assets["Y-coordinate"]
    ),
    crs="EPSG:27700"
)
```

This converts the cleaned asset table into a GeoDataFrame using British National Grid coordinates.

### Preliminary exposure scoring

```python
assets["preliminary_exposure_score"] = (
    assets["proximity_score"] + assets["capacity_score"]
)

assets["screening_category"] = assets["preliminary_exposure_score"].apply(
    assign_screening_category
)
```

This combines proximity and installed-capacity scores into a transparent Low / Medium / High screening view.

---

## Outputs

The project produces:

- a cleaned operational asset table
- a GeoJSON spatial asset layer
- exposure proxy features
- scored asset-level outputs
- regional exposure summaries
- charts for screening category distribution and regional concentration

Main output files include:

```text
data/processed/operational_energy_assets_27700.geojson
data/processed/operational_energy_assets_exposure_features.geojson
data/processed/operational_energy_assets_scored.geojson
data/processed/operational_energy_assets_scored.csv

outputs/tables/headline_metrics.csv
outputs/tables/final_regional_exposure_summary.csv
outputs/tables/top_25_assets_for_review.csv

outputs/figures/operational_energy_assets_points.png
outputs/figures/asset_boundary_proxy_map.png
outputs/figures/results_screening_category_distribution.png
outputs/figures/top_regions_high_screening_count.png
```

---

## Skills demonstrated

- Python data cleaning
- pandas
- GeoPandas
- geospatial asset mapping
- coordinate reference systems
- data-quality checks
- exposure feature engineering
- transparent risk scoring
- regional aggregation
- model limitation documentation
- analytical communication

---

## Interpretation

The output should be interpreted as a prioritisation tool.

A higher score means that an asset combines higher proximity to the chosen proxy and/or higher installed capacity.

It does not estimate probability of flooding, heat-stress intensity, physical damage, engineering failure, insured loss, financial loss or replacement cost.

The main value of the project is the transparent workflow: raw data to cleaned asset universe, geospatial layer, exposure features, scoring, summaries and limitations.

---

## Limitations

| Limitation | Why it matters |
|---|---|
| Boundary proxy is not a formal hazard layer | It cannot be interpreted as true flood, heat or coastal exposure |
| Installed capacity is not asset value | It does not measure replacement cost, insured value or revenue exposure |
| No vulnerability functions are used | The model does not estimate damage or failure probability |
| No formal climate scenario data is included | The model is not yet forward-looking under warming pathways |
| The asset universe focuses on renewable energy | Wider transport and infrastructure assets are not yet included |

---

## Next steps

Future versions could improve the model by adding Environment Agency flood zones, coastal proximity layers, heat stress layers, transport infrastructure assets, criticality proxies, score-weight sensitivity testing, an interactive dashboard and scenario-based exposure analysis.

---

## Project files

[Data Cleaning](https://github.com/jauricestudios/jaurice-market-notes/blob/main/projects/physical-climate-risk-uk-energy/notebooks/02_asset_data_cleaning.ipynb) ·
[Spatial Layer](https://github.com/jauricestudios/jaurice-market-notes/blob/main/projects/physical-climate-risk-uk-energy/notebooks/03_create_spatial_asset_layer.ipynb) ·
[Exposure Features](https://github.com/jauricestudios/jaurice-market-notes/blob/main/projects/physical-climate-risk-uk-energy/notebooks/04_geospatial_exposure_features.ipynb) ·
[Scoring](https://github.com/jauricestudios/jaurice-market-notes/blob/main/projects/physical-climate-risk-uk-energy/notebooks/05_exposure_scoring.ipynb) ·
[Results](https://github.com/jauricestudios/jaurice-market-notes/blob/main/projects/physical-climate-risk-uk-energy/notebooks/06_results_and_interpretation.ipynb)

---

## Project repository

[View project folder on GitHub](https://github.com/jauricestudios/jaurice-market-notes/tree/main/projects/physical-climate-risk-uk-energy)
