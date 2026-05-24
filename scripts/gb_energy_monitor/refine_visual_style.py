from pathlib import Path

path = Path("_static/gb_energy_monitor/dashboard.html")
html = path.read_text(encoding="utf-8")

# 1. Calm the background down: less neon, more professional dark navy.
old_background = """body {
  margin:0;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif;
  background:
    radial-gradient(circle at 15% 0%, rgba(56,189,248,.20), transparent 28%),
    radial-gradient(circle at 85% 8%, rgba(168,85,247,.16), transparent 28%),
    var(--bg);
  color:var(--text);
}"""

new_background = """body {
  margin:0;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif;
  background:
    radial-gradient(circle at 15% 0%, rgba(56,189,248,.08), transparent 24%),
    radial-gradient(circle at 85% 0%, rgba(168,85,247,.06), transparent 24%),
    #070b12;
  color:var(--text);
}"""

html = html.replace(old_background, new_background)

# 2. Make the hero more institutional.
html = html.replace(
    "<h1>Is GB energy getting tighter or looser?</h1>",
    "<h1>GB Energy Tightness Monitor</h1>\n      <p class=\"hero-question\">Is the system moving from comfortable → watchful → tight?</p>"
)

# 3. Add CSS for the subtitle and badge.
extra_css = """
.hero-question {
  margin: -4px 0 18px;
  color: #c7d7ea;
  font-size: 21px;
  font-weight: 600;
  letter-spacing: -0.02em;
}
.prototype-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 14px;
  border: 1px solid rgba(245,158,11,.45);
  background: rgba(245,158,11,.10);
  color: #ffedd5;
  border-radius: 999px;
  padding: 8px 11px;
  font-size: 12px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: .08em;
}
.prototype-badge::before {
  content: "";
  width: 8px;
  height: 8px;
  border-radius: 999px;
  background: var(--amber);
  box-shadow: 0 0 14px var(--amber);
}
"""

html = html.replace("</style>", extra_css + "\n</style>")

# 4. Insert the badge above the hero title.
html = html.replace(
    '<div class="eyebrow">Market intelligence prototype</div>',
    '<div class="prototype-badge">Prototype / manual data</div>\n      <div class="eyebrow">Market intelligence prototype</div>',
    1
)

path.write_text(html, encoding="utf-8")
print("Refined dashboard background, hero title and prototype badge.")