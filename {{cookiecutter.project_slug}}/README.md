# {{ cookiecutter.project_name }}

## {{ cookiecutter.project_short_description }}

[![status: experimental](https://github.com/GIScience/badges/raw/master/status/experimental.svg)](https://github.com/GIScience/badges#experimental)
![build: status](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/tests.yaml/badge.svg)
{% if cookiecutter.readme_type|lower == 'detailed' %}
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

```bash
docker build -t {{ cookiecutter.project_slug }} {{ cookiecutter.project_slug }}
docker run -it {{ cookiecutter.project_slug }}
```
</details>

### Usage
Some simple examples of basic usage.

### Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create.
Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### License
Distributed under the MIT License. _See [LICENSE](./LICENSE) for more information._

### Contact
If you have any other questions please contact the author, [{{ cookiecutter.full_name }}](mailto:{{ cookiecutter.email }}?subject=[GitHub]%20{{ cookiecutter.project_slug }}).
{% else %}
### Features
A brief description of the project's primary features.

### Installation
Installation is possible via `pip` as shown below.

Unix/macOS
```bash
python3 -m pip install {{ cookiecutter.project_slug }}
```

Windows
```bash
py -m pip install {{ cookiecutter.project_slug }}
```

### Usage
Some simple examples of basic usage.

### License
Distributed under the MIT License. _See [LICENSE](./LICENSE) for more information._
{%- endif %}
