# SPDX-License-Identifier: GPL-2.0+
"""Sphinx configuration for the u_boot_pylib documentation."""

import pathlib
import sys
import tomllib

_docdir = pathlib.Path(__file__).resolve().parent
_pyproject = _docdir.parent / 'pyproject.toml'
with open(_pyproject, 'rb') as _fd:
    _meta = tomllib.load(_fd)['project']

project = 'U-Boot Python Library'
author = 'Simon Glass and contributors'
copyright = '2012-2026, Simon Glass and contributors'
release = _meta['version']
version = release

# Allow the package to be imported for autodoc, without installing it
sys.path.insert(0, str(_docdir.parent))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.napoleon',
]

# Section labels are referenced as 'document:Section title'
autosectionlabel_prefix_document = True

# Only label the top-level sections, since lower ones, such as the Fixed and
# Changed headings of each release in the changelog, are not unique
autosectionlabel_maxdepth = 2

# The docstrings use the Google style ('Args:', 'Returns:')
napoleon_google_docstring = True
napoleon_numpy_docstring = False

autodoc_member_order = 'bysource'

# The Claude agent SDK is optional, so do not require it to build the docs
autodoc_mock_imports = ['claude_agent_sdk']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = []

# Keep the table of contents fully expanded in the sidebar, so clicking
# a section does not collapse the rest of the navigation.
html_theme_options = {
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
}
