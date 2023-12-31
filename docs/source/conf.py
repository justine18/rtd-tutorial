# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.append(os.path.abspath('../../src/'))

# -- Project information

project = 'GAMSPy'
copyright = "2023,  GAMS Development Corporation"
author = "Muhammet Soyturk"

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    "nbsphinx",
    "sphinx_copybutton",
    "numpydoc"
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['../_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
autosummary_generate = True
todo_include_todos = True

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# project = "GAMSpy"
# copyright = "2023, Muhammet Soyturk"
# author = "Muhammet Soyturk"
# release = "0.1.0"

# # -- General configuration ---------------------------------------------------
# # https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = [
#     "sphinx.ext.autodoc",
#     "sphinx.ext.viewcode",
#     "numpydoc",
#     "sphinx.ext.intersphinx",
#     "sphinx.ext.coverage",
#     "sphinx.ext.doctest",
#     "sphinx.ext.autosummary",
#     "sphinx.ext.graphviz",
#     "sphinx.ext.ifconfig",
#     "matplotlib.sphinxext.plot_directive",
#     "IPython.sphinxext.ipython_console_highlighting",
#     "IPython.sphinxext.ipython_directive",
#     "sphinx.ext.mathjax",
#     "sphinx_design",
#     "sphinx_copybutton",
#     "nbsphinx"
# ]

# templates_path = ["_templates"]
# exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# # -- Options for HTML output -------------------------------------------------
# # https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'sphinx_rtd_theme'
# html_static_path = ["_static"]
# html_show_sourcelink = False
# html_theme_options = {
#     "icon_links": [
#         {
#             "name": "GitHub",
#             "url": "https://github.com/GAMS-dev",
#             "icon": "fa-brands fa-square-github",
#             "type": "fontawesome",
#         },
#         {
#             "name": "Twitter",
#             "url": "https://twitter.com/GamsSoftware",
#             "icon": "fa-brands fa-square-twitter",
#         },
#     ],
#     "logo": {
#         "image_light": "_static/logo.png",
#         "image_dark": "_static/logo.png",
#     }
# }