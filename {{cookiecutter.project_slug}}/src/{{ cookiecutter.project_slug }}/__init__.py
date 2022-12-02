{%- if cookiecutter.command_line_interface|lower == 'no' -%}
from .{{ cookiecutter.project_slug }} import *
{% endif -%}
from ._version import __version__
