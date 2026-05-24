from pathlib import Path

css_path = Path("_static/custom.css")
css_path.parent.mkdir(exist_ok=True)

existing = css_path.read_text(encoding="utf-8") if css_path.exists() else ""

marker = "/* === Dark institutional green theme refinement === */"

# Remove older version if it already exists
if marker in existing:
    existing = existing.split(marker)[0].rstrip() + "\n"

extra = r"""
/* === Dark institutional green theme refinement === */

/* Main palette */
html[data-theme="dark"] {
  --pst-color-background: #00140f;
  --pst-color-on-background: #001f18;
  --pst-color-surface: #06251e;
  --pst-color-on-surface: #f4fff9;
  --pst-color-text-base: #f4fff9;
  --pst-color-text-muted: #b8d2ca;
  --pst-color-border: rgba(190, 255, 225, 0.16);
  --pst-color-primary: #28d7a0;
  --pst-color-secondary: #38bdf8;
  --pst-color-link: #7dd3fc;
  --pst-color-link-hover: #bae6fd;
}

/* Overall background */
body {
  background:
    radial-gradient(circle at 15% 0%, rgba(56,189,248,0.06), transparent 24%),
    radial-gradient(circle at 85% 0%, rgba(40,215,160,0.05), transparent 26%),
    #00140f !important;
}

/* Main article area */
.bd-article {
  background: #00251c !important;
  color: #f4fff9 !important;
}

/* Main content width */
.bd-main .bd-content .bd-article-container {
  max-width: 1020px;
}

/* Left sidebar */
.bd-sidebar-primary {
  background: #000f0b !important;
  border-right: 1px solid rgba(190,255,225,0.12) !important;
}

.bd-sidebar-primary .sidebar-primary-items__start,
.bd-sidebar-primary .sidebar-primary-items__end {
  background: #000f0b !important;
}

/* Left sidebar links */
.bd-sidebar-primary a {
  color: #a9c7be !important;
}

.bd-sidebar-primary a:hover {
  color: #7dd3fc !important;
}

.bd-sidebar-primary a.current,
.bd-sidebar-primary .current > a {
  color: #38bdf8 !important;
  font-weight: 750;
}

/* Right contents sidebar */
.bd-sidebar-secondary {
  background: #001812 !important;
  border-left: 1px solid rgba(190,255,225,0.12) !important;
}

.bd-sidebar-secondary a {
  color: #c8e7dd !important;
}

.bd-sidebar-secondary a.current {
  background: rgba(125,211,252,0.13) !important;
  color: #eaffff !important;
}

/* Headings */
.bd-article h1,
.bd-article h2,
.bd-article h3 {
  color: #fffdf4 !important;
}

.bd-article h2 {
  margin-top: 2rem;
}

/* Links/buttons */
.bd-article a {
  color: #7dd3fc;
}

.bd-article a:hover {
  color: #bae6fd;
}

/* Tables */
.bd-article table {
  background: rgba(0, 20, 15, 0.32);
  border: 1px solid rgba(190,255,225,0.14);
}

.bd-article th {
  background: rgba(0, 15, 11, 0.5);
  color: #eaffff;
}

.bd-article td {
  border-color: rgba(190,255,225,0.12);
}

/* Horizontal rules */
.bd-article hr {
  border-color: rgba(190,255,225,0.14);
}

/* Code-style button links from your theme */
.sd-btn,
.home-btn,
.bd-article a.sd-btn {
  border-radius: 8px !important;
}
"""

css_path.write_text(existing + "\n" + extra, encoding="utf-8")
print("Wrote darker institutional green theme refinement.")
