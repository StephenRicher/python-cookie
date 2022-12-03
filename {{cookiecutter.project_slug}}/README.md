# {{ cookiecutter.project_name }}

## {{ cookiecutter.project_short_description }}

[![status: experimental](https://github.com/GIScience/badges/raw/master/status/experimental.svg)](https://github.com/GIScience/badges#experimental)
![build: status](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/tests.yaml/badge.svg)
{% if cookiecutter.readme_type|lower == 'detailed' %}
### Table of contents
* [Features](#features)
* [Installation](#installation)
  * [Unix/macOS](#unixmacos)
  * [Windows](#windows)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

### Features
A brief description of the projects primary features.

### Installation
Installation is possible via `pip` as shown below.

```bash
pip install {{ cookiecutter.project_slug }}
```

However, to manage dependencies and avoid conflicts it is recommended to install within a virtual environment.

#### Unix/macOS
Run the following commands via Terminal.

```bash
python -m venv {{ cookiecutter.project_slug }}
source esneft_tools/bin/activate
pip install {{ cookiecutter.project_slug }}
```

#### Windows
Run the following commands via PowerShell.

```PowerShell
py -m venv {{ cookiecutter.project_slug }}
{{ cookiecutter.project_slug }}/Scripts/Activate.ps1
pip install {{ cookiecutter.project_slug }}
```

If running scripts is disabled on your system then run the following command before activating your environment.

```PowerShell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

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
A brief description of the projects primary features.

### Installation
```bash
pip install {{ cookiecutter.project_slug }}
```

### Usage
Some simple examples of basic usage.

### License
Distributed under the MIT License. _See [LICENSE](./LICENSE) for more information._
{%- endif %}
