from pathlib import Path

css_path = Path("_static/custom.css")
existing = css_path.read_text(encoding="utf-8") if css_path.exists() else ""

marker = "/* === Remove large green article slab === */"

if marker in existing:
    existing = existing.split(marker)[0].rstrip() + "\n"

extra = r"""
/* === Remove large green article slab === */

/* Let the full page background show through */
.bd-article {
  background: transparent !important;
}

/* Make the central content area feel like it sits on the page, not inside one big block */
.bd-main,
.bd-content,
.bd-article-container,
.bd-page-width {
  background: transparent !important;
}

/* Darker overall site background */
body {
  background:
    radial-gradient(circle at 18% 0%, rgba(56,189,248,0.055), transparent 26%),
    radial-gradient(circle at 88% 0%, rgba(34,197,94,0.04), transparent 28%),
    #000d0a !important;
}

/* Keep the sidebars clearly separated */
.bd-sidebar-primary {
  background: #000b08 !important;
}

.bd-sidebar-secondary {
  background: rgba(0, 18, 13, 0.92) !important;
}

/* Add subtle separation to the actual readable content */
.bd-article h1,
.bd-article h2,
.bd-article h3,
.bd-article p,
.bd-article table,
.bd-article ul,
.bd-article ol {
  max-width: 900px;
}

/* Make horizontal rules softer */
.bd-article hr {
  border-color: rgba(190,255,225,0.12) !important;
}

/* Reduce the feeling of one huge flat section */
.bd-article > section {
  background: transparent !important;
}
"""

css_path.write_text(existing + "\n" + extra, encoding="utf-8")
print("Removed large green article slab.")
