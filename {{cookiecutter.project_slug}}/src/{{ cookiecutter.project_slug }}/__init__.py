{%- if cookiecutter.command_line_interface|lower == 'no' -%}
from .{{ cookiecutter.project_slug }} import *
{% endif -%}
try:
    from importlib.metadata import version
    __version__ = version("{{ cookiecutter.project_slug }}")
except ModuleNotFoundError:
    __version__ = None # Required for python 3.7 compatibility
