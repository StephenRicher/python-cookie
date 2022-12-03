# Python Cookiecutter

## A simple template for building template modules and command-line interfaces in Python.

### Table of contents
  * [Features](#features)
  * [Project Structure](#project-structure)
  * [Quickstart](#quickstart)
  * [Recommended Setup](#recommended-setup)
  * [Selecting a Build Mode](#selecting-a-build-mode)
    * [1. Package Only](#1-package-only)
    * [2. Command Line Interface (without subcommands)](#2-command-line-interface-without-subcommands)
    * [3. Command Line Interface (with subcommands)](#2-command-line-interface-with-subcommands)
  * [License](#license)
  * [Contact](#contact)


### Features
Outline key project features

### Project Structure
```bash
project
│   README.md            # Write documentation here.
│   LICENSE    
│   Dockerfile
│   pyproject.toml       # Update package version and dependencies etc.
│   mkdocs.yml           # (Optional) MkDocs mode only
│   .gitignore
│   .dockerignore
│   
└───src
│   │
│   └───project
│       │   __init__.py
│       │   project.py   # Write public-facing code, for user import, here.
│       │   utils.py     # Write non-public code here.
│       │   cli.py       # (Optional) Command line mode only
│   
└───tests                # Write all your tests here.
│   │   test_project.py
│   
└───docs                 # (Optional) MkDocs mode only
│   │   about.md
│   │   index.md
│   │   installation.md
│   │   reference.md
│  
└───.github               # GitHub workflows will run all tests on push.
  │
  └───workflows
      │   tests.yaml
```


## Quickstart
Follow these steps to install dependencies and configure your Cookiecutter template.

<details>
  <summary><strong>1. Install the latest cookiecutter if you haven't installed it yet.</strong></summary>

  Unix/macOS
  ```bash
  python3 -m pip install --upgrade cookiecutter
  ```

  Windows
  ```bash
  py -m pip install --upgrade twine cookiecutter
  ```
</details>


<details>
  <summary><strong>2. Generate and configure the cookiecutter Python package.</strong></summary>

  ```bash
  cookiecutter https://github.com/StephenRicher/python-cookie.git
  ```
</details>


<details>
  <summary><strong>3. Install tools for Packaging and Documentation.</strong></summary>

  Unix/macOS
  ```bash
  python3 -m pip install --upgrade twine setuptools mkdocs mkdocstrings[python]
  ```

  Windows
  ```bash
  py -m pip install --upgrade twine setuptools mkdocs mkdocstrings[python]
  ```
</details>


## Recommended Setup
Following template creation, follow these steps to get you started.

<details>
  <summary><strong>1. Change directory into your package.</strong></summary>
  
  Unix/macOS
  ```bash
  cd package_name
  ```

  Windows
  ```bash
  cd package_name
  ```
</details>

<details>
  <summary><strong>2. Create a Git repository.</strong></summary>

  ```bash
  git init
  git add .
  git commit -m "Initial commit"
  ```
</details>

<details>
  <summary><strong>3. Install an editable version of your package to your system.</strong></summary>

  Unix/macOS
  ```bash
  python3 -m pip install .
  ```

  Windows
  ```bash
  py -m pip install .
  ```
</details>

<details>
  <summary><strong>4. Take a look at the default MkDocs template (optional).</strong></summary>

  ```bash
  mkdocs serve
  ```
</details>

<details>
  <summary><strong>5. Begin modifying the template and building your package!</strong></summary>

  ```python
  def hello(name: str = 'World') -> str:
      """Say hello.

      Args:
          name: Who to say hello to.

      Returns:
          A friendly hello.

      """
      return f'Hello {name}'
  ```
</details>

<details>
  <summary><strong>6. Upload your code to TestPyPI.</strong></summary>

  Unix/macOS
  ```bash
  python3 -m build
  python3 -m twine upload --repository testpypi dist/*
  ```
  Windows
  ```bash
  py -m build
  py -m twine upload --repository testpypi dist/*
  ```
</details>


## Selecting a Build Mode
During setup the user will be prompted to select one of three possible build modes.

**Note: The following example uses the default example functions of the template and assumes the user has built the cookiecutter with default settings.**

### 1. Package Only
Package modules without a command-line interface.

```python
>>> from number_test import prime, fibonacci
>>> prime(42)
False
>>> fibonacci(233)
True
>>>
```


### 2. Command Line Interface (_without_ subcommands)
Standard command line interface with single point of entry.

```console
stephen@pc:$ number_test --help
usage: number_test [-h] [--version] [--verbose] [number]

Boilerplate package with example numerical tests.

positional arguments:
  number      A number to test primality (default: 42)

optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit
  --verbose   verbose logging for debugging

Stephen Richer, (stephen.richer@proton.me)
```


### 3. Command Line Interface (_with_ sub-commands)
Command line interface with sub-commands offering multiple entry points.

```console
stephen@pc:$ number_test --help
usage: number_test [-h] [--version] [--verbose] Commands ...

Boilerplate package with example numerical tests.

optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit
  --verbose   verbose logging for debugging

required commands:

  Commands    Description:
    prime     Check if a number is prime.
    fib       Check if a number is part of the fibonacci sequence.

Stephen Richer, (stephen.richer@proton.me)
```


### License
Distributed under the MIT License. _See [LICENSE](./LICENSE) for more information._


### Contact
If you have any other questions please contact the author, [Stephen Richer](mailto:stephen.richer@proton.me?subject=[GitHub]%20python-cookie).
