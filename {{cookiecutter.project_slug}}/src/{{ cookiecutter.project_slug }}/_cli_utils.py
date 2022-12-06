#!/usr/bin/env python3

""" Helper functions for CLI """

import logging
import argparse
from timeit import default_timer


def _executeCommand(args):
    """ Handle function calls after argument parsing """
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
