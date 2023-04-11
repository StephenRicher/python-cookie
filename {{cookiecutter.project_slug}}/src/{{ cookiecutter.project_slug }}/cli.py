#!/usr/bin/env python3

""" {{ cookiecutter.project_short_description }} """


import sys
import logging
from timeit import default_timer
from {{ cookiecutter.project_slug }} import __version__
from ._cli_utils import OptionsParser, IntRange
{%- if cookiecutter.command_line_interface|lower == 'yes (with subcommand)' %}
from .{{ cookiecutter.project_slug }} import prime, fibonacci
{% else %}
from .{{ cookiecutter.project_slug }} import prime
{% endif %}

class CLIParser(OptionsParser):
    def __init__(self, argv: list[str] | None = None,
                 epilog: str = '', version: str = ''):
        OptionsParser.__init__(self, argv, epilog, version)

    def parse_args(self):
        {% if cookiecutter.command_line_interface|lower == 'yes (with subcommand)' %}
        parser, subparser = self.prepare_subparser()
        # HINT: Add your each subcommand and arguments to a new subparser.
        # HINT: Refer to https://docs.python.org/3/library/argparse.html
        sp1 = subparser.add_parser(
            'prime',
            description=prime_cli.__doc__.splitlines()[0],
            help='Check if a number is prime.',
            parents=[self.base_parser],
            epilog=parser.epilog)
        # HINT: Add (default: %(default)s)') to help message if you have a default.
        sp1.add_argument('number', type=IntRange(10,100), help='A number to test.')
        # HINT: For each subcommand, define an entry-point function.
        sp1.set_defaults(function=prime_cli)

        # HINT: Create a new sub-parser with disctinct arguments.
        sp2 = subparser.add_parser(
            'fib',
            description=fibonacci_cli.__doc__.splitlines()[0],
            help='Check if a number is part of the fibonacci sequence.',
            parents=[self.base_parser],
            epilog=parser.epilog)
        sp2.add_argument('number', type=int, help='A number to check.')
        sp2.set_defaults(function=fibonacci_cli)

        args = parser.parse_args(self.argv)
        self._validate_subcommand(args, parser)
        {% else %}
        parser = self.prepare_parser()
        # HINT: Add your command-line arguments here.
        # HINT: Add (default: %(default)s)') to help message if you have a default.
        # HINT: Refer to https://docs.python.org/3/library/argparse.html
        parser.add_argument('number', type=int, help='A number to test primality')
        # HINT: Define an entry-point function to pass command-line arguments.
        parser.set_defaults(function=prime_cli)
        args = parser.parse_args(self.argv)
        {%- endif %}
        return args


def main(argv: list[str] | None = None) -> int | None:
    epilog = 'Stephen Richer, (stephen.richer@proton.me)'
    logFormat = '%(asctime)s - %(levelname)s - %(funcName)s - %(message)s'
    args = CLIParser(argv, epilog, __version__).parse_args()
    if args.verbose >= 2:
        level = logging.DEBUG
    elif args.verbose == 1:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(level=level, format=logFormat)
    del args.verbose
    del args.command
    # Pop main function and excute script
    function = args.__dict__.pop('function')
    start = default_timer()
    rc = function(**vars(args))
    end = default_timer()
    logging.info(f'Total execution time: {end - start:.3f} seconds.')
    logging.shutdown()
    return rc


# HINT: CLI entry-point function which takes command-line arguments.
def prime_cli(number: int) -> bool:
    """ Check if an input number is prime. """
    if prime(number):
        print(f'{number} is a prime number!')
    else:
        print(f'{number} is not a prime number!')

{% if cookiecutter.command_line_interface|lower == 'yes (with subcommand)' %}
def fibonacci_cli(number: int) -> bool:
    """ Check if an input number is prime. """
    if fibonacci(number):
        print(f'{number} is part of the fibonacci sequence!')
    else:
        print(f'{number} is not part of the fibonacci sequence!')

{% endif %}
