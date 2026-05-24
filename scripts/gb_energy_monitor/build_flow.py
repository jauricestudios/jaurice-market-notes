from pathlib import Path
import plotly.graph_objects as go

OUT = Path("_static/gb_energy_monitor")
OUT.mkdir(parents=True, exist_ok=True)

labels = [
    "UKCS / North Sea",
    "Norway",
    "LNG imports",
    "Europe interconnectors",
    "GB gas system",
    "Households & business",
    "Industry",
    "CCGT power generation",
    "Storage / exports"
]

source = [0, 1, 2, 3, 4, 4, 4, 4]
target = [4, 4, 4, 4, 5, 6, 7, 8]
value =  [25, 35, 20, 10, 30, 12, 28, 20]

fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=18,
        thickness=18,
        line=dict(color="rgba(255,255,255,0.25)", width=0.5),
        label=labels,
        color=[
            "#20e3b2", "#20e3b2", "#4da3ff", "#ffa500",
            "#ffffff", "#9be7c8", "#9be7c8", "#ffcc66", "#d0d0d0"
        ]
    ),
    link=dict(
        source=source,
        target=target,
        value=value,
        color="rgba(32, 227, 178, 0.22)"
    )
)])

fig.update_layout(
    title="Prototype GB gas system flow",
    template="plotly_dark",
    height=470,
    margin=dict(l=20, r=20, t=60, b=20),
    paper_bgcolor="#071b16",
    plot_bgcolor="#071b16",
    font=dict(color="#f4fff8", size=13)
)

fig.write_html(
    OUT / "flow.html",
    include_plotlyjs="cdn",
    full_html=True
)

print("Built flow diagram at _static/gb_energy_monitor/flow.html")
