# {{ cookiecutter.project_name }}

## {{ cookiecutter.project_short_description }}

[![status: experimental](https://github.com/GIScience/badges/raw/master/status/experimental.svg)](https://github.com/GIScience/badges#experimental)
![build: status](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/tests.yaml/badge.svg)

## Table of contents

* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

## Features

A brief description of the projects primary features.

## Installation

Installation is possible via `pip` as shown below.

Unix/macOS
```bash
python3 -m pip install {{ cookiecutter.project_slug }}
```

Windows
```bash
py -m pip install {{ cookiecutter.project_slug }}
```

#### Alternative Install Methods (optional)

<details>
  <summary><strong>1. Install within a Virtual Environment</strong></summary>

<details>
  <summary><strong>Unix/macOS</strong></summary>

```bash
python -m venv {{ cookiecutter.project_slug }}
source {{ cookiecutter.project_slug }}/bin/activate
python3 -m pip install {{ cookiecutter.project_slug }}
```
</details>

<details>
  <summary><strong>Windows</strong></summary>

```bash
py -m venv {{ cookiecutter.project_slug }}
{{ cookiecutter.project_slug }}/Scripts/Activate.ps1
py -m pip install {{ cookiecutter.project_slug }}
```

If running scripts is disabled on your system then run the following command before activating your environment.

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
</details>
</details>

<details>
<summary><strong>2. Install within a Docker container</strong></summary>

See [here](./docker/README.md) for detailed guidance.

</details>

## Usage

{% if cookiecutter.command_line_interface|lower == 'no' -%}
```python
>>> from {{ cookiecutter.project_slug }} import prime, fibonacci
>>> prime(42)
False
>>> fibonacci(233)
True
>>>
```
{%- endif -%}
{% if cookiecutter.command_line_interface|lower == 'yes (with subcommand)' -%}
```console
stephen@pc:$ {{ cookiecutter.project_slug }} --help
usage: {{ cookiecutter.project_slug }} [-h] [--version] [--verbose] Commands ...

{{ cookiecutter.project_short_description }}

optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit
  --verbose   verbose logging for debugging

required commands:

  Commands    Description:
    prime     Check if a number is prime.
    fib       Check if a number is part of the fibonacci sequence.

{{ cookiecutter.full_name.replace('\"', '\\\"') }}, ({{ cookiecutter.email }})
```
{%- endif -%}
{% if cookiecutter.command_line_interface|lower == 'yes (without subcommand)' -%}
```console
stephen@pc:$ {{ cookiecutter.project_slug }} --help
usage: {{ cookiecutter.project_slug }} [-h] [--version] [--verbose] [number]

{{ cookiecutter.project_short_description }}

positional arguments:
  number      A number to test primality (default: 42)

optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit
  --verbose   verbose logging for debugging

{{ cookiecutter.full_name.replace('\"', '\\\"') }}, ({{ cookiecutter.email }})
```
{%- endif %}

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create.
Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

See [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed guidance.

## License

Distributed under the MIT License. _See [LICENSE](./LICENSE) for more information._

### Contact

If you have any other questions please contact the author, [{{ cookiecutter.full_name }}](mailto:{{ cookiecutter.email }}?subject=[GitHub]%20{{ cookiecutter.project_slug }}).
