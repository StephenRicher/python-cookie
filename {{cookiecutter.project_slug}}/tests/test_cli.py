#!/usr/bin/env python3

import pytest
{%- if cookiecutter.command_line_interface|lower == 'yes (with subcommand)' %}
from {{ cookiecutter.project_slug }}.cli import CLIParser, prime_cli, fibonacci_cli
{%- else %}
from {{ cookiecutter.project_slug }}.cli import CLIParser, prime_cli
{%- endif %}

{% if cookiecutter.command_line_interface|lower == 'yes (with subcommand)' %}
@pytest.mark.parametrize('argv, errror_code', [
    ([], 2),
    (['fib'], 2),
    (['prime'], 2),
    (['--version'], 0),
    (['fib', '--version'], 0),
    (['prime', '--version'], 0),
    (['invalid_command'], 2)
])
def test_CLIParser_exit(argv, errror_code):
    with pytest.raises(SystemExit) as e:
            CLIParser(argv=argv).parse_args()
    assert e.type == SystemExit
    assert e.value.code == errror_code


@pytest.mark.parametrize('argv, number, verbose, command, function', [
    (['fib', '10'], 10, 0, 'fib', fibonacci_cli),
    (['prime', '10'], 10, 0, 'prime', prime_cli),
    (['prime', '--verbose', '10'], 10, 1, 'prime', prime_cli),
    (['prime', '--verbose', '--verbose', '10'], 10, 2, 'prime', prime_cli),
])
def test_CLIParser_pass(argv, number, verbose, command, function):
    args = CLIParser(argv=argv).parse_args()
    assert args.number == number
    assert args.verbose == verbose
    assert args.command == command
    assert args.function == function


@pytest.mark.parametrize('number', [
    (0),
    (1),
    (2),
    (514229),
])
def test_fibonacci_cli_true(capfd, number):
    fibonacci_cli(number)
    out, err = capfd.readouterr()
    assert out == f'{number} is part of the fibonacci sequence!\n'


@pytest.mark.parametrize('number', [
    (4),
    (6),
    (25),
])
def test_fibonacci_cli_false(capfd, number):
    fibonacci_cli(number)
    out, err = capfd.readouterr()
    assert out == f'{number} is not part of the fibonacci sequence!\n'
{%- else %}
@pytest.mark.parametrize('argv, errror_code', [
    ([], 2),
    (['--version'], 0),
])
def test_CLIParser_exit(argv, errror_code):
    with pytest.raises(SystemExit) as e:
            CLIParser(argv=argv).parse_args()
    assert e.type == SystemExit
    assert e.value.code == errror_code


@pytest.mark.parametrize('argv, number, verbose, function', [
    (['10'], 10, 0, prime_cli),
    (['--verbose', '10'], 10, 1, prime_cli),
    (['--verbose', '--verbose', '10'], 10, 2, prime_cli),
])
def test_CLIParser_pass(argv, number, verbose, function):
    args = CLIParser(argv=argv).parse_args()
    assert args.number == number
    assert args.verbose == verbose
    assert args.function == function
{%- endif %}


@pytest.mark.parametrize('number', [
    (2),
    (3),
    (11),
    (15485863),
])
def test_prime_cli_true(capfd, number):
    prime_cli(number)
    out, err = capfd.readouterr()
    assert out == f'{number} is a prime number!\n'


@pytest.mark.parametrize('number', [
    (-1),
    (0),
    (1),
    (15485862),
])
def test_prime_cli_false(capfd, number):
    prime_cli(number)
    out, err = capfd.readouterr()
    assert out == f'{number} is not a prime number!\n'
