"""Sphinx configuration."""
project = "omniml"
author = "bramai"
copyright = "2023, bramai"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
