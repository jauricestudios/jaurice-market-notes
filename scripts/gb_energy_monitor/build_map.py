from pathlib import Path
import pandas as pd
import folium

OUT = Path("_static/gb_energy_monitor")
OUT.mkdir(parents=True, exist_ok=True)

assets = pd.DataFrame([
    {
        "name": "South Hook LNG",
        "type": "LNG Terminal",
        "lat": 51.684,
        "lon": -5.075,
        "role": "Major LNG import terminal",
        "market": "Links UK gas supply to global LNG markets and Asian JKM competition."
    },
    {
        "name": "Dragon LNG",
        "type": "LNG Terminal",
        "lat": 51.690,
        "lon": -5.030,
        "role": "LNG import terminal",
        "market": "Additional flexible LNG supply into the GB gas system."
    },
    {
        "name": "Isle of Grain LNG",
        "type": "LNG Terminal",
        "lat": 51.430,
        "lon": 0.690,
        "role": "Large LNG import terminal",
        "market": "High sendout can loosen UK gas balance and reduce stress."
    },
    {
        "name": "Bacton Gas Terminal",
        "type": "Gas Terminal / Interconnector Hub",
        "lat": 52.850,
        "lon": 1.480,
        "role": "Major gas entry and interconnector area",
        "market": "Important for UKCS, Norwegian and European gas flow sensitivity."
    },
    {
        "name": "Easington Gas Terminal",
        "type": "Gas Terminal",
        "lat": 53.650,
        "lon": 0.120,
        "role": "Major gas terminal",
        "market": "Part of the physical gas supply system into GB."
    },
    {
        "name": "St Fergus Gas Terminal",
        "type": "Gas Terminal",
        "lat": 57.560,
        "lon": -1.850,
        "role": "Major Scottish gas terminal",
        "market": "Important northern gas entry point."
    },
    {
        "name": "IFA Interconnector",
        "type": "Power Interconnector",
        "lat": 51.096,
        "lon": 1.205,
        "role": "GB-France electricity interconnector",
        "market": "Power flows respond to price spreads between GB and France."
    },
    {
        "name": "BritNed Interconnector",
        "type": "Power Interconnector",
        "lat": 51.445,
        "lon": 1.390,
        "role": "GB-Netherlands electricity interconnector",
        "market": "Shows whether GB is importing/exporting power against Europe."
    },
    {
        "name": "NSL Interconnector",
        "type": "Power Interconnector",
        "lat": 55.000,
        "lon": -1.450,
        "role": "GB-Norway electricity interconnector",
        "market": "Connects GB power to Norwegian hydro flexibility."
    }
])

colour_map = {
    "LNG Terminal": "blue",
    "Gas Terminal": "green",
    "Gas Terminal / Interconnector Hub": "green",
    "Power Interconnector": "orange"
}

m = folium.Map(
    location=[54.5, -2.2],
    zoom_start=6,
    tiles="CartoDB dark_matter"
)

for _, row in assets.iterrows():
    popup = f"""
    <div style="font-family:Arial; width:260px;">
        <h3>{row['name']}</h3>
        <b>Type:</b> {row['type']}<br>
        <b>Role:</b> {row['role']}<br><br>
        <b>Market relevance:</b><br>
        {row['market']}
    </div>
    """
    folium.CircleMarker(
        location=[row["lat"], row["lon"]],
        radius=8,
        color=colour_map.get(row["type"], "gray"),
        fill=True,
        fill_opacity=0.85,
        popup=folium.Popup(popup, max_width=320),
        tooltip=f"{row['name']} | {row['type']}"
    ).add_to(m)

legend = """
<div style="
position: fixed;
bottom: 30px;
left: 30px;
z-index: 9999;
background: rgba(0,0,0,0.75);
color: white;
padding: 12px;
border-radius: 10px;
font-family: Arial;
font-size: 13px;
">
<b>GB Energy Infrastructure</b><br>
<span style="color:#4da3ff;">●</span> LNG terminal<br>
<span style="color:#50d878;">●</span> Gas terminal<br>
<span style="color:#ffa500;">●</span> Power interconnector
</div>
"""
m.get_root().html.add_child(folium.Element(legend))

m.save(OUT / "map.html")
print("Built interactive map at _static/gb_energy_monitor/map.html")
