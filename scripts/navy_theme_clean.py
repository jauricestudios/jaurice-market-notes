from pathlib import Path

css_path = Path("_static/custom.css")
css_path.parent.mkdir(exist_ok=True)

existing = css_path.read_text(encoding="utf-8") if css_path.exists() else ""

marker = "/* === CLEAN NAVY PORTFOLIO THEME === */"

# Remove older active theme experiments if present
for old_marker in [
    "/* === ACTIVE THEME EXPERIMENT === */",
    "/* === Dark institutional green theme refinement === */",
    "/* === Final homepage theme balance tweak === */",
    "/* === Remove large green article slab === */",
    "/* === CLEAN NAVY PORTFOLIO THEME === */",
]:
    if old_marker in existing:
        existing = existing.split(old_marker)[0].rstrip() + "\n"

extra = r"""
/* === CLEAN NAVY PORTFOLIO THEME === */

/* Core colour palette */
html[data-theme="dark"] {
  --pst-color-background: #07111f;
  --pst-color-on-background: #0b1627;
  --pst-color-surface: #101d31;
  --pst-color-on-surface: #f8fafc;
  --pst-color-text-base: #f8fafc;
  --pst-color-text-muted: #b9c7d6;
  --pst-color-border: rgba(148, 163, 184, 0.20);
  --pst-color-primary: #60a5fa;
  --pst-color-secondary: #38bdf8;
  --pst-color-link: #93c5fd;
  --pst-color-link-hover: #bfdbfe;
}

/* Whole page background: navy, not too dark */
body {
  background:
    radial-gradient(circle at 18% 0%, rgba(96,165,250,0.12), transparent 26%),
    radial-gradient(circle at 85% 0%, rgba(56,189,248,0.07), transparent 28%),
    #07111f !important;
  color: #f8fafc !important;
}

/* Main article area */
.bd-article {
  background: #0b1627 !important;
  color: #f8fafc !important;
  border-left: 1px solid rgba(148,163,184,0.14);
  border-right: 1px solid rgba(148,163,184,0.14);
  padding-left: 2rem;
  padding-right: 2rem;
}

/* Content width */
.bd-main .bd-content .bd-article-container {
  max-width: 980px;
}

/* Left sidebar */
.bd-sidebar-primary {
  background: #050b14 !important;
  border-right: 1px solid rgba(148,163,184,0.16) !important;
}

.bd-sidebar-primary .sidebar-primary-items__start,
.bd-sidebar-primary .sidebar-primary-items__end {
  background: #050b14 !important;
}

/* Sidebar search box */
.bd-sidebar-primary input,
.bd-search input {
  background: #111827 !important;
  border: 1px solid rgba(148,163,184,0.24) !important;
  color: #f8fafc !important;
}

/* Sidebar links */
.bd-sidebar-primary a {
  color: #b9c7d6 !important;
}

.bd-sidebar-primary a:hover {
  color: #93c5fd !important;
}

.bd-sidebar-primary a.current,
.bd-sidebar-primary .current > a {
  color: #60a5fa !important;
  font-weight: 750;
}

/* Right contents sidebar */
.bd-sidebar-secondary {
  background: #07111f !important;
  border-left: 1px solid rgba(148,163,184,0.16) !important;
}

.bd-sidebar-secondary a {
  color: #cbd5e1 !important;
}

.bd-sidebar-secondary a.current {
  background: rgba(96,165,250,0.16) !important;
  color: #ffffff !important;
  border-left: 3px solid #60a5fa;
  border-radius: 6px;
}

/* Top bar */
.bd-header,
.bd-header-article {
  background: #07111f !important;
  border-bottom: 1px solid rgba(148,163,184,0.14) !important;
}

/* Typography: clean with slight italic headings */
.bd-article h1 {
  font-family: Georgia, "Times New Roman", serif !important;
  font-style: italic !important;
  font-weight: 800 !important;
  letter-spacing: -0.035em !important;
  color: #ffffff !important;
}

.bd-article h2,
.bd-article h3 {
  font-family: Georgia, "Times New Roman", serif !important;
  font-style: italic !important;
  font-weight: 760 !important;
  letter-spacing: -0.025em !important;
  color: #f8fafc !important;
}

/* Body text stays modern and readable */
.bd-article p,
.bd-article li,
.bd-article td,
.bd-article th {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif !important;
  color: #e5edf5 !important;
  line-height: 1.72;
}

/* Links */
.bd-article a {
  color: #93c5fd !important;
}

.bd-article a:hover {
  color: #bfdbfe !important;
}

/* Button-like markdown links */
.bd-article p a {
  font-weight: 700;
}

/* Horizontal rules */
.bd-article hr {
  border-color: rgba(148,163,184,0.16) !important;
}

/* Tables */
.bd-article table {
  background: rgba(15, 23, 42, 0.60) !important;
  border: 1px solid rgba(148,163,184,0.20) !important;
}

.bd-article th {
  background: rgba(30, 41, 59, 0.72) !important;
  color: #ffffff !important;
}

.bd-article td {
  border-color: rgba(148,163,184,0.16) !important;
}

/* Code/button badges already used on your links */
.sd-btn,
.home-btn,
.bd-article a.sd-btn {
  border-radius: 8px !important;
}

/* Optional: make the logo/sidebar image feel cleaner */
.bd-sidebar-primary img {
  border-radius: 10px;
}
"""

css_path.write_text(existing + "\n" + extra, encoding="utf-8")
print("Applied clean navy portfolio theme.")
