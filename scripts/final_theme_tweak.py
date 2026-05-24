from pathlib import Path

css_path = Path("_static/custom.css")
existing = css_path.read_text(encoding="utf-8") if css_path.exists() else ""

marker = "/* === Final homepage theme balance tweak === */"

if marker in existing:
    existing = existing.split(marker)[0].rstrip() + "\n"

extra = r"""
/* === Final homepage theme balance tweak === */

/* Slightly less flat green, more institutional dark green/navy */
body {
  background:
    radial-gradient(circle at 20% 0%, rgba(56,189,248,0.055), transparent 25%),
    radial-gradient(circle at 85% 0%, rgba(34,197,94,0.045), transparent 28%),
    #000f0b !important;
}

/* Main reading area: dark forest green but less bright */
.bd-article {
  background: #002118 !important;
}

/* Content column: slightly tighter and cleaner */
.bd-main .bd-content .bd-article-container {
  max-width: 960px;
}

/* Left sidebar: stronger separation */
.bd-sidebar-primary {
  background: #000b08 !important;
  box-shadow: inset -1px 0 0 rgba(190,255,225,0.10);
}

/* Right sidebar: reduce visual weight */
.bd-sidebar-secondary {
  background: #00120d !important;
  border-left: 1px solid rgba(190,255,225,0.10) !important;
}

.bd-sidebar-secondary a.current {
  background: rgba(125,211,252,0.10) !important;
  border-left: 3px solid #38bdf8;
}

/* Make text slightly more premium/readable */
.bd-article p,
.bd-article li {
  line-height: 1.75;
}

/* Better project section spacing */
.bd-article h2 {
  padding-top: 0.4rem;
  margin-top: 2.2rem;
}

.bd-article h3 {
  margin-top: 1.8rem;
}

/* Make buttons a bit sharper */
.bd-article a.reference.internal,
.bd-article a.reference.external {
  font-weight: 650;
}
"""

css_path.write_text(existing + "\n" + extra, encoding="utf-8")
print("Applied final homepage theme balance tweak.")
