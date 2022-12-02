#!/usr/bin/env python

""" The setup script. """


import os
from setuptools import setup, find_namespace_packages


def read(file: str):
    with open(os.path.join(os.path.dirname(__file__), file)) as fh:
        return fh.read()


def get_info():
    info = {}
    versionPath = 'src/{{ cookiecutter.project_slug }}/_version.py'
    with open(versionPath) as fp:
        exec(fp.read(), info)
    return info


setup(
    name='{{ cookiecutter.project_slug }}',
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    python_requires='>=3.7.0',
    install_requires=[],
    license='MIT',
    classifiers=[
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    {%- if 'no' not in cookiecutter.command_line_interface|lower %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:parseArgs',
        ],
    },
    {%- endif %}
    version=get_info()['__version__'],
    description='{{ cookiecutter.project_short_description }}',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    keywords='{{ cookiecutter.project_slug }}',
    packages=find_namespace_packages(where='src'),
    package_dir={'': 'src'},
    zip_safe=False,
)
