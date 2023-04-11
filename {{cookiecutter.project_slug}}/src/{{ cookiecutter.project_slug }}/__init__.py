{%- if cookiecutter.command_line_interface|lower == 'no' -%}
from .{{ cookiecutter.project_slug }} import *
{% endif -%}
from importlib.metadata import version
__version__ = version("{{ cookiecutter.project_slug }}")
