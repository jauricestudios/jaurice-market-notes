from pathlib import Path
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

OUT = Path("_static/gb_energy_monitor")
OUT.mkdir(parents=True, exist_ok=True)

generation = pd.DataFrame({
    "fuel": ["Wind", "Gas", "Nuclear", "Solar", "Biomass", "Imports"],
    "mw": [14500, 9000, 5200, 1800, 2300, 1200]
})

fig = make_subplots(
    rows=2,
    cols=2,
    specs=[
        [{"type": "indicator"}, {"type": "indicator"}],
        [{"type": "bar", "colspan": 2}, None],
    ],
    subplot_titles=("GB Demand", "System Signal", "Generation by Fuel Type")
)

fig.add_trace(
    go.Indicator(
        mode="number",
        value=34.0,
        number={"suffix": " GW"},
        title={"text": "Current GB Demand"}
    ),
    row=1,
    col=1
)

fig.add_trace(
    go.Indicator(
        mode="number+delta",
        value=55,
        delta={"reference": 50},
        title={"text": "Energy Stress Score / 100"}
    ),
    row=1,
    col=2
)

fig.add_trace(
    go.Bar(
        x=generation["fuel"],
        y=generation["mw"],
        text=generation["mw"],
        textposition="auto",
        name="MW"
    ),
    row=2,
    col=1
)

fig.update_layout(
    title="GB Energy System Monitor",
    height=850,
    template="plotly_dark",
    margin=dict(l=40, r=40, t=80, b=40)
)

fig.write_html(
    OUT / "dashboard.html",
    include_plotlyjs="cdn",
    full_html=True
)

print("Built _static/gb_energy_monitor/dashboard.html")
