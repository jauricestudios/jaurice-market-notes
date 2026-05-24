from pathlib import Path
import sys

theme = sys.argv[1] if len(sys.argv) > 1 else "navy"

css_path = Path("_static/custom.css")
css_path.parent.mkdir(exist_ok=True)
existing = css_path.read_text(encoding="utf-8") if css_path.exists() else ""

marker = "/* === ACTIVE THEME EXPERIMENT === */"
if marker in existing:
    existing = existing.split(marker)[0].rstrip() + "\n"

themes = {
    "navy": {
        "body": "#050914",
        "article": "#07111f",
        "sidebar": "#03070d",
        "right": "#050b14",
        "accent": "#38bdf8",
        "link": "#7dd3fc",
        "muted": "#b7c7d9",
    },
    "green_navy": {
        "body": "#020f0d",
        "article": "#061f1d",
        "sidebar": "#020b09",
        "right": "#041311",
        "accent": "#2dd4bf",
        "link": "#67e8f9",
        "muted": "#b9d7d0",
    },
    "terminal": {
        "body": "#050505",
        "article": "#090d0c",
        "sidebar": "#030303",
        "right": "#060807",
        "accent": "#22c55e",
        "link": "#86efac",
        "muted": "#b8c7bd",
    },
}

if theme not in themes:
    raise SystemExit(f"Unknown theme: {theme}. Use navy, green_navy, or terminal.")

c = themes[theme]

extra = f"""
/* === ACTIVE THEME EXPERIMENT === */
/* Theme: {theme} */

html[data-theme="dark"] {{
  --pst-color-background: {c["body"]};
  --pst-color-on-background: {c["article"]};
  --pst-color-surface: {c["article"]};
  --pst-color-on-surface: #f8fafc;
  --pst-color-text-base: #f8fafc;
  --pst-color-text-muted: {c["muted"]};
  --pst-color-border: rgba(148, 163, 184, 0.18);
  --pst-color-primary: {c["accent"]};
  --pst-color-secondary: {c["link"]};
  --pst-color-link: {c["link"]};
  --pst-color-link-hover: #e0f2fe;
}}

body {{
  background:
    radial-gradient(circle at 18% 0%, color-mix(in srgb, {c["accent"]} 13%, transparent), transparent 24%),
    radial-gradient(circle at 88% 0%, rgba(168,85,247,0.06), transparent 28%),
    {c["body"]} !important;
}}

.bd-article {{
  background: {c["article"]} !important;
  color: #f8fafc !important;
  border-left: 1px solid rgba(148,163,184,0.10);
  border-right: 1px solid rgba(148,163,184,0.10);
  padding-left: 2rem;
  padding-right: 2rem;
}}

.bd-main .bd-content .bd-article-container {{
  max-width: 980px;
}}

.bd-sidebar-primary {{
  background: {c["sidebar"]} !important;
  border-right: 1px solid rgba(148,163,184,0.13) !important;
}}

.bd-sidebar-primary .sidebar-primary-items__start,
.bd-sidebar-primary .sidebar-primary-items__end {{
  background: {c["sidebar"]} !important;
}}

.bd-sidebar-secondary {{
  background: {c["right"]} !important;
  border-left: 1px solid rgba(148,163,184,0.13) !important;
}}

.bd-sidebar-primary a {{
  color: {c["muted"]} !important;
}}

.bd-sidebar-primary a.current,
.bd-sidebar-primary .current > a,
.bd-sidebar-primary a:hover {{
  color: {c["link"]} !important;
}}

.bd-sidebar-secondary a {{
  color: {c["muted"]} !important;
}}

.bd-sidebar-secondary a.current {{
  background: rgba(56,189,248,0.12) !important;
  color: #ffffff !important;
  border-left: 3px solid {c["accent"]};
}}

.bd-article h1,
.bd-article h2,
.bd-article h3 {{
  color: #ffffff !important;
}}

.bd-article p,
.bd-article li {{
  color: #e5edf5 !important;
  line-height: 1.72;
}}

.bd-article hr {{
  border-color: rgba(148,163,184,0.14) !important;
}}

.bd-article a {{
  color: {c["link"]} !important;
}}

.bd-article table {{
  background: rgba(255,255,255,0.025);
  border: 1px solid rgba(148,163,184,0.16);
}}

.bd-article th {{
  background: rgba(255,255,255,0.045);
  color: #ffffff;
}}

.bd-article td {{
  border-color: rgba(148,163,184,0.14);
}}

"""

css_path.write_text(existing + "\n" + extra, encoding="utf-8")
print(f"Applied theme: {theme}")
