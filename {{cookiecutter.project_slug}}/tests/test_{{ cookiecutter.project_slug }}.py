#!/usr/bin/env python3


def test_import():
    """ Test if module successfully imports """
    try:
        import {{ cookiecutter.project_slug }}
    except ModuleNotFoundError as exc:
        assert False, exc
