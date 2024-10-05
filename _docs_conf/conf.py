# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import autoapi

project = "solfege"
copyright = "2024, mshafer1"
author = "mshafer1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx_mdinclude",
    "sphinx.ext.autodoc.typehints",
]

extensions.append("autoapi.extension")

autoapi_dirs = ["../solfege"]
autodoc_typehints = "description"
templates_path = ["_templates"]
autoapi_template_dir = "_templates/autoapi"


autoapi_options = list(autoapi.extension._DEFAULT_OPTIONS)
autoapi_options.remove("private-members")

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
