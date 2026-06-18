title: Jaurice O'Connor
author: Jaurice O'Connor
copyright: "2026"

exclude_patterns:
  - .venv_energy/**
  - _build/**
  - .DS_Store
  - "**.ipynb_checkpoints"
  - intro_backup*.md
  - intro_old.md

execute:
  execute_notebooks: force

repository:
  url: https://github.com/jauricestudios/jaurice-market-notes
  branch: main

html:
  use_repository_button: true
  use_download_button: false
  use_fullscreen_button: true

sphinx:
  config:
    html_theme: sphinx_book_theme

    html_static_path:
      - _static

    html_css_files:
      - custom.css

    html_title: "Jaurice O'Connor | Energy Research"

    html_theme_options:
      default_mode: light
      navbar_start:
        - navbar-logo
      show_navbar_depth: 1
      navigation_with_keys: false
