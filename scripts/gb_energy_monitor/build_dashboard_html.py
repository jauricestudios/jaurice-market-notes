from pathlib import Path
import pandas as pd
import plotly.graph_objects as go

OUT = Path("_static/gb_energy_monitor")
OUT.mkdir(parents=True, exist_ok=True)

# Prototype dummy data for the first visual shell.
# Later this gets replaced by Elexon/National Gas/GIE API data.
generation = pd.DataFrame({
    "fuel": ["Wind", "Gas / CCGT", "Nuclear", "Solar", "Biomass", "Imports"],
    "mw": [14500, 9000, 5200, 1800, 2300, 1200]
})

demand_gw = 34.0
wind_share = 42.6
ccgt_gw = 9.0
net_imports_gw = 1.2
stress_score = 55

fig = go.Figure()
fig.add_trace(go.Bar(
    x=generation["fuel"],
    y=generation["mw"],
    text=generation["mw"],
    textposition="auto",
    marker=dict(color="#20e3b2")
))

fig.update_layout(
    title="Generation by fuel type",
    template="plotly_dark",
    height=420,
    margin=dict(l=45, r=25, t=60, b=40),
    paper_bgcolor="#071b16",
    plot_bgcolor="#071b16",
    font=dict(color="#f3fff8"),
    yaxis_title="MW"
)

chart_html = fig.to_html(full_html=False, include_plotlyjs="cdn")

html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>GB Energy Stress Monitor</title>
<style>
    body {{
        margin: 0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        background: #031f18;
        color: #f4fff8;
    }}

    .wrap {{
        max-width: 1180px;
        margin: 0 auto;
        padding: 28px;
    }}

    .hero {{
        border: 1px solid rgba(32, 227, 178, 0.35);
        background: linear-gradient(135deg, #062d23, #020f0c);
        border-radius: 22px;
        padding: 28px;
        box-shadow: 0 12px 35px rgba(0,0,0,0.35);
    }}

    .eyebrow {{
        color: #20e3b2;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        font-size: 12px;
        font-weight: 700;
    }}

    h1 {{
        margin: 8px 0 8px;
        font-size: 38px;
        line-height: 1.05;
    }}

    .subtitle {{
        color: #c7e9dc;
        max-width: 850px;
        font-size: 16px;
        line-height: 1.55;
    }}

    .signal {{
        margin-top: 18px;
        display: inline-block;
        background: rgba(32, 227, 178, 0.12);
        border: 1px solid rgba(32, 227, 178, 0.4);
        color: #ffffff;
        padding: 10px 14px;
        border-radius: 999px;
        font-weight: 700;
    }}

    .cards {{
        display: grid;
        grid-template-columns: repeat(6, minmax(0, 1fr));
        gap: 14px;
        margin: 22px 0;
    }}

    .card {{
        background: #071b16;
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 18px;
        padding: 16px;
        min-height: 92px;
    }}

    .card-label {{
        color: #9fb8af;
        font-size: 12px;
        margin-bottom: 10px;
    }}

    .card-value {{
        font-size: 27px;
        font-weight: 800;
    }}

    .card-note {{
        color: #b9d4ca;
        font-size: 12px;
        margin-top: 8px;
    }}

    .grid {{
        display: grid;
        grid-template-columns: 1.15fr 0.85fr;
        gap: 18px;
        margin-top: 18px;
    }}

    .panel {{
        background: #061814;
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 20px;
        padding: 20px;
    }}

    h2 {{
        margin-top: 0;
        font-size: 22px;
    }}

    p {{
        line-height: 1.58;
        color: #e5fff4;
    }}

    table {{
        width: 100%;
        border-collapse: collapse;
        font-size: 14px;
    }}

    th, td {{
        border-bottom: 1px solid rgba(255,255,255,0.12);
        padding: 10px;
        text-align: left;
        vertical-align: top;
    }}

    th {{
        color: #20e3b2;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }}

    .tag {{
        display: inline-block;
        border: 1px solid rgba(32,227,178,0.35);
        color: #dcfff2;
        border-radius: 999px;
        padding: 6px 10px;
        margin: 4px 4px 0 0;
        font-size: 12px;
        background: rgba(32,227,178,0.08);
    }}

    .chart {{
        margin-top: 18px;
        border-radius: 20px;
        overflow: hidden;
        border: 1px solid rgba(255,255,255,0.12);
    }}

    .footer-note {{
        color: #abc8bd;
        font-size: 13px;
        margin-top: 18px;
    }}

    @media (max-width: 950px) {{
        .cards {{
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }}
        .grid {{
            grid-template-columns: 1fr;
        }}
    }}
</style>
</head>
<body>
<div class="wrap">

    <section class="hero">
        <div class="eyebrow">GB power · gas · LNG · storage · interconnectors</div>
        <h1>GB Energy Stress Monitor</h1>
        <div class="subtitle">
            A Python-built market monitor tracking the physical drivers behind UK energy tightness:
            demand, wind output, gas burn, LNG availability, interconnector flows, storage and European benchmark pressure.
        </div>
        <div class="signal">System signal: Balanced but watchful · Prototype score {stress_score}/100</div>
    </section>

    <section class="cards">
        <div class="card">
            <div class="card-label">GB demand</div>
            <div class="card-value">{demand_gw:.1f} GW</div>
            <div class="card-note">How much electricity the system needs.</div>
        </div>
        <div class="card">
            <div class="card-label">Wind share</div>
            <div class="card-value">{wind_share:.1f}%</div>
            <div class="card-note">High wind reduces gas burn.</div>
        </div>
        <div class="card">
            <div class="card-label">Gas / CCGT</div>
            <div class="card-value">{ccgt_gw:.1f} GW</div>
            <div class="card-note">Gas being burned for power.</div>
        </div>
        <div class="card">
            <div class="card-label">Net imports</div>
            <div class="card-value">{net_imports_gw:.1f} GW</div>
            <div class="card-note">Interconnector dependence.</div>
        </div>
        <div class="card">
            <div class="card-label">UK gas signal</div>
            <div class="card-value">Elevated</div>
            <div class="card-note">NBP/UK gas still needs monitoring.</div>
        </div>
        <div class="card">
            <div class="card-label">Stress score</div>
            <div class="card-value">{stress_score}/100</div>
            <div class="card-note">Composite prototype signal.</div>
        </div>
    </section>

    <section class="grid">
        <div class="panel">
            <h2>Today’s market read</h2>
            <p>
                The prototype signal is <b>balanced but watchful</b>. Wind output is assumed to be strong enough
                to reduce gas-fired generation, which lowers immediate gas burn from the power sector.
                The main risk to monitor is whether lower wind, higher demand, weaker LNG sendout or tighter
                European storage conditions push the system toward higher gas and power stress.
            </p>
            <p>
                The purpose of this dashboard is not just to show prices. It is to explain whether the GB energy
                system is becoming <b>looser or tighter</b>, and which physical driver is responsible.
            </p>
        </div>

        <div class="panel">
            <h2>Skills demonstrated</h2>
            <span class="tag">Python data pipeline</span>
            <span class="tag">pandas cleaning</span>
            <span class="tag">Plotly dashboard</span>
            <span class="tag">SQL / SQLite layer</span>
            <span class="tag">GIS / GeoPandas map</span>
            <span class="tag">Excel analyst workbook</span>
            <span class="tag">Market commentary</span>
            <p class="footer-note">
                This project is designed as a full analyst workflow: Python collects data, SQL stores it,
                GIS maps infrastructure, Excel provides a business-facing workbook, and the website communicates the market signal.
            </p>
        </div>
    </section>

    <section class="chart">
        {chart_html}
    </section>

    <section class="grid">
        <div class="panel">
            <h2>Driver framework</h2>
            <table>
                <tr><th>Driver</th><th>Stress rises when...</th><th>Stress falls when...</th></tr>
                <tr><td>Weather</td><td>Cold and low wind</td><td>Warm and windy</td></tr>
                <tr><td>Wind output</td><td>Wind is weak, CCGTs run harder</td><td>Wind is strong, gas burn falls</td></tr>
                <tr><td>LNG</td><td>Cargoes are scarce or Asia bids higher</td><td>Cargoes are abundant into Europe/UK</td></tr>
                <tr><td>Storage</td><td>Storage is low for the season</td><td>Storage is full or injections are ahead</td></tr>
                <tr><td>Interconnectors</td><td>GB relies heavily on imports</td><td>GB has surplus and exports</td></tr>
                <tr><td>TTF / Europe</td><td>European gas rallies</td><td>European gas weakens</td></tr>
            </table>
        </div>

        <div class="panel">
            <h2>Pipeline architecture</h2>
            <table>
                <tr><th>Layer</th><th>Tool</th><th>Output</th></tr>
                <tr><td>Ingestion</td><td>Python</td><td>Elexon, National Gas, GIE, market CSVs</td></tr>
                <tr><td>Storage</td><td>SQL / SQLite</td><td>Queryable time-series database</td></tr>
                <tr><td>Spatial layer</td><td>GeoPandas / Folium</td><td>LNG terminals, gas entry points, interconnectors</td></tr>
                <tr><td>Business layer</td><td>Excel</td><td>Pivot tables, weekly summary, scenario checks</td></tr>
                <tr><td>Publishing</td><td>GitHub Pages</td><td>Interactive public monitor</td></tr>
            </table>
        </div>
    </section>

    <p class="footer-note">
        Prototype note: current values are illustrative. The next version replaces them with public/live datasets and adds the GIS map and downloadable Excel workbook.
    </p>

</div>
</body>
</html>
"""

(OUT / "dashboard.html").write_text(html, encoding="utf-8")
print("Built improved dashboard at _static/gb_energy_monitor/dashboard.html")
