from pathlib import Path

OUT = Path("_static/gb_energy_monitor")
OUT.mkdir(parents=True, exist_ok=True)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>GB Energy Tightness Monitor</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
:root {
  --bg:#080b14;
  --panel:#101827;
  --panel2:#151f32;
  --text:#f4f7fb;
  --muted:#a8b3c7;
  --line:rgba(255,255,255,.12);
  --blue:#38bdf8;
  --orange:#f97316;
  --purple:#a855f7;
  --teal:#14b8a6;
  --red:#ef4444;
  --green:#22c55e;
  --amber:#f59e0b;
}
* { box-sizing:border-box; }
body {
  margin:0;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif;
  background:
    radial-gradient(circle at 15% 0%, rgba(56,189,248,.20), transparent 28%),
    radial-gradient(circle at 85% 8%, rgba(168,85,247,.16), transparent 28%),
    var(--bg);
  color:var(--text);
}
.wrap { max-width:1500px; margin:0 auto; padding:24px; }
.top {
  display:flex; justify-content:space-between; align-items:center; gap:16px;
  background:rgba(16,24,39,.88); border:1px solid var(--line);
  border-radius:18px; padding:14px 18px; position:sticky; top:12px; z-index:10;
  backdrop-filter:blur(12px);
}
.logo { font-weight:900; font-size:18px; }
.sub { color:var(--muted); font-size:12px; margin-top:3px; }
.nav { display:flex; gap:8px; flex-wrap:wrap; }
.nav span {
  border:1px solid var(--line); border-radius:999px; padding:7px 10px;
  color:var(--muted); font-size:12px;
}
.hero {
  margin-top:22px; display:grid; grid-template-columns:1.15fr .85fr; gap:18px;
}
.card, .panel {
  background:linear-gradient(180deg, rgba(21,31,50,.96), rgba(11,18,32,.96));
  border:1px solid var(--line); border-radius:24px; padding:24px;
  box-shadow:0 20px 50px rgba(0,0,0,.30);
}
.hero-main {
  border-color:rgba(56,189,248,.35);
  background:linear-gradient(135deg, rgba(56,189,248,.16), rgba(249,115,22,.10), rgba(168,85,247,.12)), var(--panel);
}
.eyebrow {
  color:var(--blue); text-transform:uppercase; letter-spacing:.16em;
  font-size:12px; font-weight:900;
}
h1 { font-size:64px; line-height:.95; letter-spacing:-.06em; margin:14px 0; }
h2 { margin:0 0 14px; font-size:24px; letter-spacing:-.03em; }
p { color:#dbe7f5; line-height:1.58; }
.signal {
  display:inline-flex; gap:9px; align-items:center; margin-top:18px;
  border:1px solid rgba(245,158,11,.45); background:rgba(245,158,11,.12);
  padding:11px 14px; border-radius:999px; font-weight:900;
}
.dot { width:10px; height:10px; background:var(--amber); border-radius:999px; box-shadow:0 0 18px var(--amber); }
.kpis {
  display:grid; grid-template-columns:repeat(5, 1fr); gap:14px; margin-top:18px;
}
.kpi {
  background:var(--panel2); border:1px solid var(--line);
  border-radius:18px; padding:17px; min-height:126px;
}
.kpi small { display:block; color:var(--muted); margin-bottom:8px; }
.kpi b { font-size:26px; }
.kpi p { font-size:12px; margin:8px 0 0; color:#b8c6d8; }
.grid2 { display:grid; grid-template-columns:1fr 1fr; gap:18px; margin-top:18px; }
.grid1 { display:grid; grid-template-columns:1fr; gap:18px; margin-top:18px; }
table { width:100%; border-collapse:collapse; font-size:14px; }
th, td { border-bottom:1px solid var(--line); padding:11px 9px; text-align:left; vertical-align:top; }
th { color:#8fdcff; font-size:11px; text-transform:uppercase; letter-spacing:.09em; }
.badge { display:inline-block; padding:5px 9px; border-radius:999px; font-weight:800; font-size:12px; }
.elevated { background:rgba(249,115,22,.18); color:#fed7aa; border:1px solid rgba(249,115,22,.35); }
.watch { background:rgba(168,85,247,.18); color:#e9d5ff; border:1px solid rgba(168,85,247,.35); }
.high { background:rgba(239,68,68,.18); color:#fecaca; border:1px solid rgba(239,68,68,.35); }
.normal { background:rgba(34,197,94,.18); color:#bbf7d0; border:1px solid rgba(34,197,94,.35); }
.tag {
  display:inline-block; margin:4px; padding:8px 10px; border-radius:999px;
  border:1px solid var(--line); background:rgba(255,255,255,.04); color:#dbeafe; font-size:12px;
}
iframe { width:100%; border:0; border-radius:18px; background:#050816; }
.note { color:var(--muted); font-size:13px; margin-top:20px; }
@media(max-width:1100px) {
  .hero, .grid2 { grid-template-columns:1fr; }
  .kpis { grid-template-columns:repeat(2,1fr); }
  h1 { font-size:44px; }
}
</style>
</head>

<body>
<div class="wrap">

  <div class="top">
    <div>
      <div class="logo">GB Energy Tightness Monitor</div>
      <div class="sub">Power · Gas · LNG · Storage · Interconnectors · Analyst Signals</div>
    </div>
    <div class="nav">
      <span>Market watchlist</span>
      <span>Infrastructure map</span>
      <span>Gas flow</span>
      <span>Stress scale</span>
      <span>Data stack</span>
    </div>
  </div>

  <section class="hero">
    <div class="card hero-main">
      <div class="eyebrow">Market intelligence prototype</div>
      <h1>Is GB energy getting tighter or looser?</h1>
      <p>
        This monitor connects physical energy drivers to market pressure:
        power demand, wind, CCGT gas burn, LNG sendout, storage, interconnectors,
        TTF, JKM and wider commodity risk.
      </p>
      <div class="signal"><span class="dot"></span> Signal: Balanced but watchful · Tightness score 55/100</div>
    </div>

    <div class="card">
      <h2>Today’s analyst read</h2>
      <p>
        Wind is assumed to be reducing gas-fired generation, which loosens immediate gas burn.
        The risk is that lower wind, higher demand, weaker LNG sendout, lower storage or stronger TTF/JKM pricing
        pushes GB toward a tighter gas and power balance.
      </p>
      <p><b>Core question:</b> is the system moving from comfortable → watchful → tight?</p>
    </div>
  </section>

  <section class="kpis">
    <div class="kpi"><small>UK Gas</small><b style="color:var(--orange)">117p/therm</b><p>Elevated vs normal-ish 50p area.</p></div>
    <div class="kpi"><small>TTF Gas</small><b style="color:var(--purple)">€48/MWh</b><p>European benchmark pressure.</p></div>
    <div class="kpi"><small>LNG JKM</small><b style="color:var(--purple)">$18.81</b><p>Asia LNG pull risk.</p></div>
    <div class="kpi"><small>Wind share</small><b style="color:var(--blue)">42.6%</b><p>High wind reduces CCGT burn.</p></div>
    <div class="kpi"><small>Tightness score</small><b style="color:var(--amber)">55/100</b><p>Prototype composite signal.</p></div>
  </section>

  <section class="grid2">
    <div class="panel">
      <h2>Market watchlist</h2>
      <table>
        <tr><th>Market</th><th>Level</th><th>Signal</th><th>Why it matters</th></tr>
        <tr><td><b>UK Gas</b></td><td>117p/therm</td><td><span class="badge elevated">Elevated</span></td><td>UK home market benchmark. Around 50p is normal-ish; above 100p is elevated.</td></tr>
        <tr><td><b>TTF Gas</b></td><td>€48/MWh</td><td><span class="badge elevated">Elevated</span></td><td>Main European gas benchmark; affects UK through LNG competition and interconnectors.</td></tr>
        <tr><td><b>LNG JKM</b></td><td>$18.81/MMBtu</td><td><span class="badge watch">Watch</span></td><td>Asian LNG price. High JKM can pull cargoes away from Europe/UK.</td></tr>
        <tr><td><b>Brent</b></td><td>$103/bbl</td><td><span class="badge high">High</span></td><td>Global crude benchmark and broad energy inflation signal.</td></tr>
        <tr><td><b>Coal</b></td><td>$132/t</td><td><span class="badge watch">Watch</span></td><td>Power fuel substitute; relevant for global power and fuel-switching pressure.</td></tr>
      </table>
    </div>

    <div class="panel">
      <h2>UK gas stress scale</h2>
      <table>
        <tr><th>UK gas price</th><th>Same as</th><th>How to read it</th></tr>
        <tr><td>50p/therm</td><td>£0.50/therm</td><td><span class="badge normal">Normal-ish / comfortable</span></td></tr>
        <tr><td>100p/therm</td><td>£1.00/therm</td><td><span class="badge elevated">Elevated</span></td></tr>
        <tr><td>150p/therm</td><td>£1.50/therm</td><td>High</td></tr>
        <tr><td>200p/therm</td><td>£2.00/therm</td><td>Very high</td></tr>
        <tr><td>400p/therm</td><td>£4.00/therm</td><td><span class="badge high">Crisis-level</span></td></tr>
        <tr><td>800p/therm</td><td>£8.00/therm</td><td>Extreme historical stress</td></tr>
      </table>
    </div>
  </section>

  <section class="grid2">
    <div class="panel">
      <h2>Physical infrastructure map</h2>
      <p>Clickable GIS layer: LNG terminals, gas terminals and electricity interconnectors.</p>
      <iframe src="map.html" height="560"></iframe>
    </div>

    <div class="panel">
      <h2>GB gas flow visual</h2>
      <p>Gas enters from UKCS, Norway, LNG and Europe, then moves into demand, power burn, storage or exports.</p>
      <iframe src="flow.html" height="560"></iframe>
    </div>
  </section>

  <section class="grid2">
    <div class="panel">
      <h2>Price up / price down matrix</h2>
      <table>
        <tr><th>Driver</th><th>Price up when...</th><th>Price down when...</th><th>Meaning</th></tr>
        <tr><td>Weather</td><td>Cold, low wind</td><td>Warm, windy</td><td>Heating demand and power demand.</td></tr>
        <tr><td>Wind output</td><td>Wind weak; CCGTs run harder</td><td>Wind strong; gas burn falls</td><td>Core GB power-gas link.</td></tr>
        <tr><td>LNG</td><td>Cargoes scarce / Asia bids higher</td><td>Cargoes abundant into Europe/UK</td><td>Flexible global supply.</td></tr>
        <tr><td>Storage</td><td>Low for season / heavy withdrawals</td><td>Full / injections ahead</td><td>Security buffer.</td></tr>
        <tr><td>TTF</td><td>Europe gas rallies</td><td>Europe weakens</td><td>UK not isolated from Europe.</td></tr>
        <tr><td>JKM</td><td>Asia pulls LNG away</td><td>Asia demand weak</td><td>Global LNG competition.</td></tr>
        <tr><td>Geopolitics</td><td>War risk / chokepoints / sanctions</td><td>Risk premium fades</td><td>Adds risk premium to energy.</td></tr>
      </table>
    </div>

    <div class="panel">
      <h2>Market participants</h2>
      <table>
        <tr><th>Player</th><th>What they do</th><th>Seller or buyer?</th></tr>
        <tr><td>Producers</td><td>Extract gas from fields, e.g. Norway, UKCS, Qatar LNG.</td><td>Usually primary physical sellers.</td></tr>
        <tr><td>LNG exporters</td><td>Liquefy gas and sell cargoes.</td><td>Sellers of flexible LNG supply.</td></tr>
        <tr><td>Trading houses</td><td>Buy/sell gas, LNG and derivatives.</td><td>Can be buyers and sellers.</td></tr>
        <tr><td>Utilities / suppliers</td><td>Buy wholesale energy and sell to customers.</td><td>Often buyers; sometimes sellers.</td></tr>
        <tr><td>Power generators</td><td>Buy gas to generate electricity.</td><td>Usually buyers.</td></tr>
      </table>
    </div>
  </section>

  <section class="grid2">
    <div class="panel">
      <h2>Build evidence</h2>
      <span class="tag">Python data collection</span>
      <span class="tag">pandas cleaning</span>
      <span class="tag">SQL / SQLite storage</span>
      <span class="tag">GIS / Folium map</span>
      <span class="tag">Plotly visualisation</span>
      <span class="tag">Excel analyst workbook</span>
      <span class="tag">GitHub Pages publishing</span>
      <p>
        Final workflow: Python pulls data, SQL stores it, GIS maps physical assets,
        Excel gives a business-facing workbook, and the dashboard explains the market.
      </p>
    </div>

    <div class="panel">
      <h2>What an analyst checks next</h2>
      <table>
        <tr><th>Question</th><th>Why it matters</th></tr>
        <tr><td>Is wind falling while demand rises?</td><td>Could increase CCGT burn and tighten gas.</td></tr>
        <tr><td>Is UK gas above or below TTF after conversion?</td><td>Shows UK-specific tightness versus Europe.</td></tr>
        <tr><td>Are LNG send-outs strong?</td><td>More LNG can loosen GB gas balance.</td></tr>
        <tr><td>Are storage withdrawals heavy?</td><td>Shows short-term system stress.</td></tr>
        <tr><td>Are interconnectors importing or exporting?</td><td>Shows reliance on external markets.</td></tr>
      </table>
    </div>
  </section>

  <p class="note">
    Prototype note: current values are illustrative. Next version replaces them with real public/exported data from Elexon/BMRS,
    National Gas, GIE AGSI/ALSI and Trading Economics/market exports.
  </p>

</div>
</body>
</html>
"""

(OUT / "dashboard.html").write_text(html, encoding="utf-8")
print("Built V0.4 market-intelligence dashboard at _static/gb_energy_monitor/dashboard.html")
