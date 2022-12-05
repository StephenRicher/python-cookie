# Using {{ cookiecutter.project_name }} via Docker

This directory contains a `Dockerfile` to make it easy to build and run {{ cookiecutter.project_name }} via [Docker](https://www.docker.com/).

## 1. Install Docker

Follow the general installation instructions [on the Docker site](https://docs.docker.com/install/):

* [macOS](https://docs.docker.com/docker-for-mac/install/)
* [Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [Windows](https://docs.docker.com/docker-for-windows/install/)
{% if cookiecutter.command_line_interface|lower != 'no' %}
## 2. Build the Image

```shell
mkdir {{ cookiecutter.project_slug }}-docker
cd {{ cookiecutter.project_slug }}-docker
wget https://raw.githubusercontent.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/main/docker/Dockerfile
docker build -t {{ cookiecutter.project_slug }} .
```

where `{{ cookiecutter.project_slug }}` is the desired Docker image name.

## 3. Run the CLI

```shell
docker run --rm -it {{ cookiecutter.project_slug }} --help
```

Alternatively, to run the image without the CLI, use the following command:

```shell
docker run --rm -it --entrypoint /bin/bash {{ cookiecutter.project_slug }}
```
{% else %}
## 2. Build the Image

```
mkdir {{ cookiecutter.project_slug }}-docker
cd {{ cookiecutter.project_slug }}-docker
wget https://raw.githubusercontent.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/main/docker/Dockerfile
docker build -t {{ cookiecutter.project_slug }} .
```

where `{{ cookiecutter.project_slug }}` is the desired Docker image name.

## 3. Run an Interactive Shell

```
docker run --rm -it {{ cookiecutter.project_slug }}
```
{%- endif %}
