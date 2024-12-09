from pathlib import Path

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information ---------------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = "drake-tutorial"
copyright = "2024, Cole Ten"
author = "Cole Ten"
release = "0.0.0"
version = "0.0.0"


# -- General configuration -------------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "myst_parser",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Exclude directories ---------------------------------------------------------------
# Exclude all markdown files in the below folders unless they match the name of their
# parent directory (by convention all other sibling Markdown files in the folder are
# included in the content of the Markdown file whose name matches its parent directory)

# The directories containing documentation Markdown files.
# doc_directories = [
#     "getting_started",
#     "core_drake_concepts",
#     "core_drake_concepts/systems",
#     "core_drake_concepts/contexts",
#     "core_drake_concepts/events",
#     "core_drake_concepts/basic_simulation_outline",
#     "multibody_simulation_and_visualization",
#     "multibody_simulation_and_visualization/multibody_simulation_outline",
#     "multibody_simulation_and_visualization/scara_robot_simulation_example",
#     "using_drake_with_hardware",
#     "using_drake_with_hardware/ros2",
# ]
#
# exclude_patterns = []
# for doc_dir in doc_directories:
#     doc_dir_path = Path(doc_dir)
#     try:
#         for entry in doc_dir_path.iterdir():
#             if (
#                 entry.is_file()
#                 and entry.stem.lower() != doc_dir_path.stem.lower()
#             ):
#                 exclude_patterns.append(str(entry))
#     except OSError:
#         pass

# -- Options for HTML output -----------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_theme_options = {
    "toc_title": "Page Outline",
    "show_toc_level": 3,
    "logo": {
        "text": "Drake Tutorial",
        "image_light": "_static/drake_logo.jpg",
        "image_dark": "_static/drake_logo.jpg",
    },
}
