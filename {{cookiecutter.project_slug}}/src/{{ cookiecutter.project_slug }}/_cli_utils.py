#!/usr/bin/env python3

""" Helper functions for CLI """

import sys
import argparse
from datetime import datetime


class OptionsParser():
    def __init__(self, argv: list[str] | None = None,
                 epilog: str = '', version: str = ''):
        self.argv = argv
        self.epilog = epilog
        self.base_parser = self._get_base_parser(version)

    def prepare_subparser(self) -> tuple[argparse.ArgumentParser, argparse._SubParsersAction]:
        parser = self.prepare_parser()
        subparser = self._get_subparser(parser)
        self.subparser = True
        return parser, subparser

    def prepare_parser(self) -> argparse.ArgumentParser:
        """ Create base parser of verbose/version. """
        parser = argparse.ArgumentParser(
            epilog=self.epilog, description=__doc__,
            parents=[self.base_parser])
        return parser

    def _get_base_parser(self, version: str) -> argparse.ArgumentParser:
        """ Create base parser of verbose/version. """
        base_parser = argparse.ArgumentParser(add_help=False)
        base_parser.add_argument(
            '--version', action='version', version=f'%(prog)s {version}')
        base_parser.add_argument(
            '--verbose', action='count',
            default=0, help='verbose logging for debugging')
        return base_parser

    def _get_subparser(self, parser: argparse.ArgumentParser
                       ) -> argparse._SubParsersAction:
        subparser = parser.add_subparsers(
            title='required commands',
            description='',
            dest='command',
            metavar='Commands',
            help='Description:')
        return subparser

    def _validate_subcommand(self, args: argparse.Namespace,
                             parser: argparse.ArgumentParser) -> None:
        if (self.subparser) and ('function' not in args):
            parser.print_help()
            sys.exit()


class IntRange:
    def __init__(self, imin: int | None = None, imax: int | None = None):
        self.imin = imin
        self.imax = imax

    def __call__(self, arg: str):
        try:
            value = int(arg)
        except ValueError:
            raise self.exception()
        if ((self.imin is not None and value < self.imin)
                or (self.imax is not None and value > self.imax)):
            raise self.exception()
        return value

    def exception(self):
        if self.imin is not None and self.imax is not None:
            return argparse.ArgumentTypeError(
                f'Must be an integer in the range [{self.imin}, {self.imax}].')
        elif self.imin is not None:
            return argparse.ArgumentTypeError(
                f'Must be an integer >= {self.imin}.')
        elif self.imax is not None:
            return argparse.ArgumentTypeError(
                f'Must be an integer <= {self.imax}.')
        else:
            return argparse.ArgumentTypeError('Must be an integer.')


class FloatRange:
    def __init__(self, fmin: int | None = None, fmax: int | None = None,
                 inclusive: str = 'both'):
        assert inclusive in ['both', 'neither', 'left', 'right']
        self.fmin = fmin
        self.fmax = fmax
        self.inclusive = inclusive

    def __call__(self, arg: str):
        try:
            value = float(arg)
        except ValueError:
            raise self.exception()
        if self.fmin is not None:
            if (self.inclusive in ['both', 'left']):
                if value < self.fmin:
                    raise self.exception()
            elif value <= self.fmin:
                raise self.exception()
        if self.fmax is not None:
            if (self.inclusive in ['both', 'right']):
                if value > self.fmax:
                    raise self.exception()
            elif value >= self.fmax:
                raise self.exception()
        return value

    def exception(self):
        if self.fmin is not None and self.fmax is not None:
            l = '[' if self.inclusive in ['both', 'left'] else '('
            r = ']' if self.inclusive in ['both', 'right'] else ')'
            return argparse.ArgumentTypeError(
                f'Must be an float in the range {l}{self.fmin}, {self.fmax}{r}.')
        elif self.fmin is not None:
            op = '>=' if self.inclusive in ['both', 'left'] else '>'
            return argparse.ArgumentTypeError(
                f'Must be an float {op} {self.fmin}.')
        elif self.fmax is not None:
            op = '<=' if self.inclusive in ['both', 'right'] else '<'
            return argparse.ArgumentTypeError(
                f'Must be an float {op} {self.fmax}.')
        else:
            return argparse.ArgumentTypeError('Must be a float.')


class Date:
    def __init__(self, format: str = '%d-%m-%Y'):
        self.format = format

    def __call__(self, arg: str):
        try:
            value = datetime.strptime(arg, self.format)
        except ValueError:
            raise self.exception(arg)
        return value

    def exception(self, arg: str):
        return argparse.ArgumentTypeError(
            f"Time data '{arg}' does not match format '{self.format}'.")
