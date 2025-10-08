# docs/conf.py
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'Geometry Documentation'
author = 'Your Name'
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]
autodoc_mock_imports = ['math']
html_theme = 'sphinx_rtd_theme'
