FROM python:3.10-slim

ENV PIP_ROOT_USER_ACTION=ignore

RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    git clone --recursive --depth 1 https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }} && \
    cd {{ cookiecutter.project_slug }}/ && python3 -m pip install . && \
    apt-get autoremove -y && apt-get clean
{% if cookiecutter.command_line_interface|lower != 'no' %}
ENTRYPOINT ["{{ cookiecutter.project_slug }}"]
{% else %}
CMD ["/bin/bash"]
{%- endif %}
