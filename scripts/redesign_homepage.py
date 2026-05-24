from pathlib import Path

intro = Path("intro.md")
intro.write_text("""# Jaurice O’Connor

## Market, Infrastructure & Risk Analytics

I'm a final year Mathematics student interested in energy markets, commodities, natural catastrophe risk and physical climate risk.

My dissertation focuses on Monte Carlo methods for financial modelling, giving me experience with Python, simulation, uncertainty analysis and model evaluation. I’m now looking to apply these skills to real world problems in energy, infrastructure and risk analytics.

Alongside my studies, I’m developing projects using Python, Excel and GIS to analyse energy market dynamics, physical hazard exposure and climate related infrastructure risk. My aim is to build a career in roles that combine quantitative analysis, commercial awareness and practical risk modelling.

I'm particularly interested in analyst opportunities across energy, commodities, infrastructure risk, economic research and market analytics.

```{raw} html
<p class="home-buttons">
  <a class="home-btn primary" href="_static/gb_energy_monitor/dashboard.html">Open GB Energy Monitor</a>
  <a class="home-btn" href="projects/gb-energy-monitor/index.html">View project page</a>
</p>
<div class="project-grid">

  <div class="project-card featured">
    <div class="project-status">Active prototype</div>
    <h3>GB Energy Tightness Monitor</h3>
    <p>
      A market-intelligence dashboard tracking GB power, gas, LNG, storage and interconnector pressure.
      It is designed to answer whether the system is becoming tighter or looser, and which physical drivers explain it.
    </p>
    <div class="project-tags">
      <span>Python</span><span>Plotly</span><span>GIS/Folium</span><span>Commodities</span><span>Energy markets</span>
    </div>
    <p class="project-links">
      <a href="_static/gb_energy_monitor/dashboard.html">Open dashboard</a>
      <a href="projects/gb-energy-monitor/index.html">View notes</a>
    </p>
  </div>

  <div class="project-card">
    <div class="project-status">Prototype</div>
    <h3>Climate Infrastructure Exposure Map</h3>
    <p>
      A geospatial screening project for identifying UK energy and transport assets that may warrant closer
      physical climate-risk review.
    </p>
    <div class="project-tags">
      <span>GeoPandas</span><span>Spatial joins</span><span>Risk scoring</span><span>Infrastructure</span>
    </div>
  </div>

  <div class="project-card">
    <div class="project-status">Planned build</div>
    <h3>Geopolitical Energy Risk Monitor</h3>
    <p>
      A planned monitor for chokepoints, sanctions, war risk, shipping disruption and commodity supply exposure.
    </p>
    <div class="project-tags">
      <span>Geopolitics</span><span>Commodities</span><span>Maps</span><span>Event risk</span>
    </div>
  </div>

  <div class="project-card">
    <div class="project-status">Planned build</div>
    <h3>Copper Demand Scenario Model</h3>
    <p>
      A scenario model for studying how electrification, grid expansion and AI infrastructure could affect
      medium-term copper demand.
    </p>
    <div class="project-tags">
      <span>Economic research</span><span>Scenario modelling</span><span>Commodities</span>
    </div>
  </div>

</div>
<div class="project-grid">

  <div class="project-card featured">
    <div class="project-status">Active prototype</div>
    <h3>GB Energy Tightness Monitor</h3>
    <p>
      A market-intelligence dashboard tracking GB power, gas, LNG, storage and interconnector pressure.
      It is designed to answer whether the system is becoming tighter or looser, and which physical drivers explain it.
    </p>
    <div class="project-tags">
      <span>Python</span><span>Plotly</span><span>GIS/Folium</span><span>Commodities</span><span>Energy markets</span>
    </div>
    <p class="project-links">
      <a href="_static/gb_energy_monitor/dashboard.html">Open dashboard</a>
      <a href="projects/gb-energy-monitor/index.html">View notes</a>
    </p>
  </div>

  <div class="project-card">
    <div class="project-status">Prototype</div>
    <h3>Climate Infrastructure Exposure Map</h3>
    <p>
      A geospatial screening project for identifying UK energy and transport assets that may warrant closer
      physical climate-risk review.
    </p>
    <div class="project-tags">
      <span>GeoPandas</span><span>Spatial joins</span><span>Risk scoring</span><span>Infrastructure</span>
    </div>
  </div>

  <div class="project-card">
    <div class="project-status">Planned build</div>
    <h3>Geopolitical Energy Risk Monitor</h3>
    <p>
      A planned monitor for chokepoints, sanctions, war risk, shipping disruption and commodity supply exposure.
    </p>
    <div class="project-tags">
      <span>Geopolitics</span><span>Commodities</span><span>Maps</span><span>Event risk</span>
    </div>
  </div>

  <div class="project-card">
    <div class="project-status">Planned build</div>
    <h3>Copper Demand Scenario Model</h3>
    <p>
      A scenario model for studying how electrification, grid expansion and AI infrastructure could affect
      medium-term copper demand.
    </p>
    <div class="project-tags">
      <span>Economic research</span><span>Scenario modelling</span><span>Commodities</span>
    </div>
  </div>

</divPY
python scripts/redesign_homepage.py
jupyter-book clean .
jupyter-book build --all .
open _build/html/intro.html
