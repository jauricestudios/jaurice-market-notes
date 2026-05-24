from pathlib import Path

path = Path("_static/gb_energy_monitor/dashboard.html")
html = path.read_text(encoding="utf-8")

extra_css = """
.status-strip {
  margin-top: 18px;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
}
.status-card {
  background: rgba(16,24,39,.72);
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: 13px 14px;
}
.status-card small {
  display: block;
  color: var(--muted);
  margin-bottom: 5px;
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: .08em;
}
.status-card b {
  font-size: 14px;
}
.legend {
  margin-top: 18px;
  background: rgba(16,24,39,.72);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 14px 16px;
}
.legend-title {
  font-size: 12px;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: .10em;
  margin-bottom: 10px;
}
.legend-row {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}
.legend-chip {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  border: 1px solid var(--line);
  border-radius: 999px;
  padding: 7px 10px;
  font-size: 12px;
  color: #dbe7f5;
}
.colour-dot {
  width: 9px;
  height: 9px;
  border-radius: 999px;
}
.actions {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  margin-top: 16px;
}
.action-btn {
  border: 1px solid var(--line);
  border-radius: 999px;
  padding: 9px 12px;
  color: #eaf2ff;
  background: rgba(255,255,255,.04);
  font-size: 13px;
}
.action-btn.primary {
  border-color: rgba(56,189,248,.45);
  background: rgba(56,189,248,.10);
}
.framework-note {
  border-left: 3px solid var(--blue);
  padding-left: 12px;
  color: #dbe7f5;
  margin-top: 14px;
}
@media(max-width:1100px) {
  .status-strip { grid-template-columns: repeat(2, 1fr); }
}
@media(max-width:650px) {
  .status-strip { grid-template-columns: 1fr; }
}
"""

html = html.replace("</style>", extra_css + "\n</style>")

status_html = """
  <section class="status-strip">
    <div class="status-card">
      <small>Data status</small>
      <b>Prototype / manual values</b>
    </div>
    <div class="status-card">
      <small>Next data source</small>
      <b>Elexon BMRS generation mix</b>
    </div>
    <div class="status-card">
      <small>Refresh mode</small>
      <b>Static GitHub Pages build</b>
    </div>
    <div class="status-card">
      <small>Coverage</small>
      <b>GB power, gas, LNG, storage framework</b>
    </div>
  </section>

"""

html = html.replace("  <section class=\"hero\">", status_html + "  <section class=\"hero\">", 1)

legend_html = """
  <section class="legend">
    <div class="legend-title">Colour meaning</div>
    <div class="legend-row">
      <span class="legend-chip"><span class="colour-dot" style="background:var(--blue)"></span> Power / electricity</span>
      <span class="legend-chip"><span class="colour-dot" style="background:var(--orange)"></span> Gas / CCGT / UK NBP</span>
      <span class="legend-chip"><span class="colour-dot" style="background:var(--purple)"></span> LNG / global gas / JKM</span>
      <span class="legend-chip"><span class="colour-dot" style="background:var(--teal)"></span> Storage / system buffer</span>
      <span class="legend-chip"><span class="colour-dot" style="background:var(--red)"></span> Stress / warning</span>
      <span class="legend-chip"><span class="colour-dot" style="background:var(--muted)"></span> Pending / unknown data</span>
    </div>
  </section>

"""

html = html.replace("  <section class=\"kpis\">", legend_html + "  <section class=\"kpis\">", 1)

storage_and_terms = """
  <section class="grid2">
    <div class="panel">
      <h2>Storage interpretation</h2>
      <p>
        Storage matters because it is the system buffer. The useful question is not only whether storage is high or low,
        but whether it is high or low for the season and whether prices are reacting correctly.
      </p>
      <table>
        <tr><th>Situation</th><th>Market read</th></tr>
        <tr><td>Storage high + TTF low</td><td>Comfortable supply buffer; lower tightness.</td></tr>
        <tr><td>Storage low + TTF high</td><td>Tight market; scarcity or security premium likely.</td></tr>
        <tr><td>Storage high + TTF high</td><td>Potential risk premium, LNG competition, geopolitics or forward concern.</td></tr>
        <tr><td>Storage low + TTF low</td><td>Possible weak demand, expected supply relief or market complacency.</td></tr>
      </table>
    </div>

    <div class="panel">
      <h2>Flow definitions</h2>
      <p>
        These terms matter because gas and power prices are physical flow problems before they become chart problems.
      </p>
      <table>
        <tr><th>Term</th><th>Meaning</th></tr>
        <tr><td>Import</td><td>GB receives gas or electricity from another market.</td></tr>
        <tr><td>Export</td><td>GB sends gas or electricity to another market.</td></tr>
        <tr><td>Net import</td><td>Imports are larger than exports.</td></tr>
        <tr><td>Net export</td><td>Exports are larger than imports.</td></tr>
        <tr><td>Interconnector flow</td><td>Physical movement between GB and another country or market.</td></tr>
        <tr><td>Spread</td><td>Price difference between two markets, e.g. UK NBP versus TTF.</td></tr>
      </table>
    </div>
  </section>

"""

html = html.replace(
    "  <section class=\"grid2\">\n    <div class=\"panel\">\n      <h2>Physical infrastructure map</h2>",
    storage_and_terms + "  <section class=\"grid2\">\n    <div class=\"panel\">\n      <h2>Physical infrastructure map</h2>",
    1
)

actions_html = """
  <section class="grid1">
    <div class="panel">
      <h2>Project outputs</h2>
      <p>
        These are the outputs the finished project should provide. Some are placeholders until the real data layer is added.
      </p>
      <div class="actions">
        <a class="action-btn primary" href="../../projects/gb-energy-monitor/index.html">View project page</a>
        <a class="action-btn" href="dashboard.html">Open standalone dashboard</a>
        <a class="action-btn" href="map.html">Open infrastructure map</a>
        <a class="action-btn" href="flow.html">Open gas flow visual</a>
        <span class="action-btn">CSV export: planned</span>
        <span class="action-btn">Excel workbook: planned</span>
        <span class="action-btn">SQL database: planned</span>
      </div>
      <p class="framework-note">
        The next professional milestone is to replace manual values with real generation data, then add processed CSV,
        SQLite storage and an Excel workbook to prove the full analyst workflow.
      </p>
    </div>
  </section>

"""

html = html.replace("  <p class=\"note\">", actions_html + "  <p class=\"note\">", 1)

path.write_text(html, encoding="utf-8")
print("Polished dashboard written to _static/gb_energy_monitor/dashboard.html")