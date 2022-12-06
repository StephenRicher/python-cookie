#!/usr/bin/env python3

""" {{ cookiecutter.project_short_description }} """


import sys
import argparse
from {{ cookiecutter.project_slug }} import __version__
from ._cli_utils import _executeCommand, _getBaseParser
{%- if cookiecutter.command_line_interface|lower == 'yes (with subcommand)' %}
from .{{ cookiecutter.project_slug }} import prime, fibonacci
{% else %}
from .{{ cookiecutter.project_slug }} import prime
{% endif %}

def parseArgs() -> argparse.Namespace:
    epilog = '{{ cookiecutter.full_name.replace('\"', '\\\"') }}, ({{ cookiecutter.email }})'
    baseParser = _getBaseParser(__version__)
    parser = argparse.ArgumentParser(
        epilog=epilog, description=__doc__, parents=[baseParser])
    {% if cookiecutter.command_line_interface|lower == 'yes (with subcommand)' %}
    subparser = parser.add_subparsers(
        title='required commands',
        description='',
        dest='command',
        metavar='Commands',
        help='Description:')
    # HINT: Add your each subcommand and arguments to a new subparser.
    # HINT: Refer to https://docs.python.org/3/library/argparse.html
    sp1 = subparser.add_parser(
        'prime',
        description=prime_cli.__doc__.split('\n')[0],
        help='Check if a number is prime.',
        parents=[baseParser],
        epilog=parser.epilog)
    # HINT: Add (default: %(default)s)') to help message if you have a default.
    sp1.add_argument('number', type=int, help='A number to test primality.')
    # HINT: For each subcommand, define an entry-point function.
    sp1.set_defaults(function=prime_cli)

    # HINT: Create a new sub-parser with disctinct arguments.
    sp2 = subparser.add_parser(
        'fib',
        description=fibonacci_cli.__doc__.split('\n')[0],
        help='Check if a number is part of the fibonacci sequence.',
        parents=[baseParser],
        epilog=parser.epilog)
    sp2.add_argument('number', type=int, help='A number to check.')
    sp2.set_defaults(function=fibonacci_cli)
    {% else %}
    # HINT: Add your command-line arguments here.
    # HINT: Add (default: %(default)s)') to help message if you have a default.
    # HINT: Refer to https://docs.python.org/3/library/argparse.html
    parser.add_argument('number', type=int, help='A number to test primality')
    # HINT: Define an entry-point function to pass command-line arguments.
    parser.set_defaults(function=prime_cli)
    {%- endif %}
    args = parser.parse_args()
    if 'function' not in args:
        parser.print_help()
        sys.exit()

    return _executeCommand(args)

# HINT: CLI entry-point function which takes command-line arguments.
def prime_cli(number: int) -> bool:
    """ Check if an input number is prime. """
    if prime(number):
        print(f'{number} is a prime number!')
    else:
        print(f'{number} is not prime number!')

{% if cookiecutter.command_line_interface|lower == 'yes (with subcommand)' %}
def fibonacci_cli(number: int) -> bool:
    """ Check if an input number is prime. """
    if fibonacci(number):
        print(f'{number} is part of the fibonacci sequence!')
    else:
        print(f'{number} is not part of the fibonacci sequence!')

{% endif %}
