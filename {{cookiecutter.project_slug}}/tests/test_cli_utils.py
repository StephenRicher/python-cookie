#!/usr/bin/env python3


import pytest
import argparse
from datetime import datetime
from {{ cookiecutter.project_slug }}._cli_utils import IntRange, FloatRange, Date, OptionsParser


@pytest.mark.parametrize('imin, imax, value, expected', [
    (0, 10, '5', 5),
    (0, 10, '0', 0),
    (0, 10, '10', 10),
])
def test_IntRange_pass(imin, imax, value, expected):
    assert IntRange(imin, imax)(value) == expected


@pytest.mark.parametrize('imin, imax, value, expected', [
    (0, 10, '5.0', argparse.ArgumentTypeError),
    (0, 10, 'five', argparse.ArgumentTypeError),
    (0, 10, 20, argparse.ArgumentTypeError),
    (0, 10, -20, argparse.ArgumentTypeError),
])
def test_IntRange_fail(imin, imax, value, expected):
    with pytest.raises(expected):
        IntRange(imin, imax)(value)


@pytest.mark.parametrize('imin, imax, inclusive, value, expected', [
    (0, 10, 'both', '5.', 5),
    (0, 10, 'neither', '5.', 5),
    (0, 10, 'both', '5', 5),
    (0, 10, 'left', '0', 0),
    (0, 10, 'right', '10', 10),
])
def test_FloatRange_pass(imin, imax, inclusive, value, expected):
    assert FloatRange(imin, imax, inclusive)(value) == expected


@pytest.mark.parametrize('imin, imax, inclusive, value, expected', [
    (0, 10, 'all', '5.', AssertionError),
    (0, 10, 'both', 'five', argparse.ArgumentTypeError),
    (0, 10, 'neither', '0', argparse.ArgumentTypeError),
    (0, 10, 'neither', '10', argparse.ArgumentTypeError),
    (0, 10, 'left', '10', argparse.ArgumentTypeError),
    (0, 10, 'right', '0', argparse.ArgumentTypeError),
    (0, 10, 'both', '-20', argparse.ArgumentTypeError),
    (0, 10, 'both', '20', argparse.ArgumentTypeError),
    (0, 10, 'left', '-20', argparse.ArgumentTypeError),
    (0, 10, 'left', '20', argparse.ArgumentTypeError),
    (0, 10, 'right', '-20', argparse.ArgumentTypeError),
    (0, 10, 'right', '20', argparse.ArgumentTypeError),
    (0, 10, 'neither', '-20', argparse.ArgumentTypeError),
    (0, 10, 'neither', '20', argparse.ArgumentTypeError),
])
def test_FloatRange_fail(imin, imax, inclusive, value, expected):
    with pytest.raises(expected):
        FloatRange(imin, imax, inclusive)(value)


@pytest.mark.parametrize('format, date, expected', [
    ('%d-%m-%Y', '01-01-2023', datetime(year=2023, month=1, day=1)),
    ('%d-%b-%Y', '01-Jan-2023', datetime(year=2023, month=1, day=1)),
    ('%d-%B-%Y', '01-January-2023', datetime(year=2023, month=1, day=1)),
])
def test_Date_pass(format, date, expected):
    assert Date(format)(date) == expected


@pytest.mark.parametrize('format, date, expected', [
    ('%d-%m-%Y', '01-Jan-2023', argparse.ArgumentTypeError),
    ('%d-%m-%y', '06-31-2023', argparse.ArgumentTypeError),
])
def test_Date_fail(format, date, expected):
    with pytest.raises(expected):
        Date(format)(date)


@pytest.mark.parametrize('format, date, expected', [
    ('%d-%m-%Y', '01-01-2023', datetime(year=2023, month=1, day=1)),
    ('%d-%b-%Y', '01-Jan-2023', datetime(year=2023, month=1, day=1)),
    ('%d-%B-%Y', '01-January-2023', datetime(year=2023, month=1, day=1)),
])
def test_Date_pass(format, date, expected):
    assert Date(format)(date) == expected


def test_OptionsParser():
    op = OptionsParser(
        argv=['arg1', 'arg2'], epilog='test_epilog', version='1.0.0')
    parser = op.prepare_parser()
    assert op.version == '1.0.0'
    assert op.argv == ['arg1', 'arg2']
    assert '--version' in parser.format_usage()
    assert '--verbose' in parser.format_usage()
    assert 'test_epilog' in parser.format_help()


def test_OptionsParser_sub():
    op = OptionsParser()
    parser, subparser = op.prepare_subparser()
    assert op.subparser == True
    assert '--version' in parser.format_usage()
    assert '--verbose' in parser.format_usage()
