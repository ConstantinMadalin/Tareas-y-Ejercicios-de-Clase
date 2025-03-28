# -- Project information -----------------------------------------------------

project = 'Hospital Management'
author = 'Constantin Madalin Ismana'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('../mi_proyecto/docs'))  # Asegúrate de que Sphinx pueda encontrar tu paquete

extensions = [
    'sphinx.ext.autodoc',  # Generación automática de documentación de clases y funciones
    'sphinx.ext.napoleon', # Soporte para docstrings estilo Google y NumPy
]

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'  # Tema simple para la documentación

# -- Options for autodoc -----------------------------------------------------

autoclass_content = 'both'  # Incluye tanto la clase como el docstring
autodoc_member_order = 'bysource'  # Ordena los miembros por el orden en el código

html_static_path = []
