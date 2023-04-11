#!/usr/bin/env python3

import os
import sys
import shutil

REMOVE_PATHS = [
    '{%- if cookiecutter.command_line_interface|lower == "no" %} '
    'src/{{ cookiecutter.project_slug }}/cli.py {% endif %}',
    '{%- if cookiecutter.command_line_interface|lower == "no" %} '
    'src/{{ cookiecutter.project_slug }}/tests/test_cli.py {% endif %}',
    '{%- if cookiecutter.command_line_interface|lower == "no" %} '
    'src/{{ cookiecutter.project_slug }}/_cli_utils.py {% endif %}',
    '{%- if cookiecutter.include_mkdocs|lower == "no" %} '
    'mkdocs.yml {% endif %}',
    '{%- if cookiecutter.include_mkdocs|lower == "no" %} '
    'docs/ {% endif %}'
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)
