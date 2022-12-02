# Python Cookiecutter

## A simple template for building template modules and command-line interfaces in Python.

## Quickstart

**Install the latest Cookiecutter if you haven't installed it yet.**

```bash
pip install -U cookiecutter
```

**Install mkdocs and mkdocstrings to utilise the [MkDocs](https://www.mkdocs.org/) template (optional).**
```bash
pip install mkdocs mkdocstrings[python]
```

**Generate and configure the cookiecutter Python package.**
```bash
cookiecutter https://github.com/StephenRicher/python-cookie.git
```

**Change directory into your package.**
```bash
cd package_name
```

**Create a Git repository.**
```bash
git init .
git add .
git commit -m "Initial commit"
```

**Install an editable version of your package to your system.**
```bash
pip install -e .
```

**Take a look at the default MkDocs template (optional).**
```bash
mkdocs serve
```

**Begin modifying the template and building your package!**

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


### 2. Command-line Interface (_without_ subcommands)
Standard command line interface with single point of entry.

```shell
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


### 3. Command-line Interface (_with_ sub-commands)
Command line interface with sub-commands offering multiple entry points.

```shell
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

## License
Distributed under the MIT License. _See [LICENSE](./LICENSE) for more information._


## Contact
If you have any other questions please contact the author, [Stephen Richer](mailto:stephen.richer@proton.me?subject=[GitHub]%20python-cookie).
