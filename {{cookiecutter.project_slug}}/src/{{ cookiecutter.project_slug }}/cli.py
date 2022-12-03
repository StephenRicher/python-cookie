#!/usr/bin/env python3

""" {{ cookiecutter.project_short_description }} """


import sys
import logging
import argparse
from timeit import default_timer
from {{ cookiecutter.project_slug }} import __version__
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

    sp1 = subparser.add_parser(
        'prime',
        description=prime_cli.__doc__.split('\n')[0],
        help='Check if a number is prime.',
        parents=[baseParser],
        epilog=parser.epilog)
    sp1.add_argument(
        'number', nargs='?', type=int, default=42,
        help='A number to test primality (default: %(default)s)')
    sp1.set_defaults(function=prime_cli)

    sp2 = subparser.add_parser(
        'fib',
        description=fibonacci_cli.__doc__.split('\n')[0],
        help='Check if a number is part of the fibonacci sequence.',
        parents=[baseParser],
        epilog=parser.epilog)
    sp2.add_argument(
        'number', nargs='?', type=int, default=42,
        help='A number to check (default: %(default)s)')
    sp2.set_defaults(function=fibonacci_cli)
    {% else %}
    parser.add_argument(
        'number', nargs='?', type=int, default=42,
        help='A number to test primality (default: %(default)s)')
    parser.set_defaults(function=prime_cli)
    {%- endif %}

    args = parser.parse_args()
    if 'function' not in args:
        parser.print_help()
        sys.exit()

    return _executeCommand(args)


def _executeCommand(args):
    # Initialise logging
    logFormat = '%(asctime)s - %(levelname)s - %(funcName)s - %(message)s'
    logging.basicConfig(level=args.verbose, format=logFormat)
    del args.verbose
    {%- if cookiecutter.command_line_interface|lower == 'yes (with subcommand)' %}
    del args.command
    {%- endif %}
    # Pop main function and excute script
    function = args.__dict__.pop('function')
    start = default_timer()
    rc = function(**vars(args))
    end = default_timer()
    logging.info(f'Total execution time: {end - start:.3f} seconds.')
    logging.shutdown()
    return rc


def _getBaseParser(version: str) -> argparse.Namespace:
    """ Create base parser of verbose/version. """
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        '--version', action='version', version='%(prog)s {}'.format(version))
    parser.add_argument(
        '--verbose', action='store_const', const=logging.DEBUG,
        default=logging.ERROR, help='verbose logging for debugging')
    return parser


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
