#!/usr/bin/env python3

""" {{ cookiecutter.project_short_description }} """

import math
import logging


logger = logging.getLogger(__name__)
{% if cookiecutter.command_line_interface|lower == 'no' %}
# Functions directly accessible from module level
__all__ = ['prime', 'fibonacci']
{% else %}

def prime_cli(number: int) -> bool:
    """ Check if an input number is prime. """
    if prime(number):
        print(f'{number} is a prime number!')
    else:
        print(f'{number} is not prime number!')
{% endif %}
{% if cookiecutter.command_line_interface|lower == 'yes (with subcommand)' %}
def fibonacci_cli(number: int) -> bool:
    """ Check if an input number is prime. """
    if fibonacci(number):
        print(f'{number} is part of the fibonacci sequence!')
    else:
        print(f'{number} is not part of the fibonacci sequence!')

{% endif %}

def prime(number: int = 42) -> bool:
    """ Check if a number is prime.

    This function is a template illustrating best practise docstring style.

    :param int number: A number to test primality.
    :returns: A boolean value
    :rtype: bool
    """
    if number < 2:
        logger.info(f'{number} is less than 2.')
        return False
    elif number % 2 == 0:
        logger.info(f'{number} is even.')
        return number == 2
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def fibonacci(number: int = 42) -> bool:
    """ Check if a number is part of the fibonacci sequence.

    This function is a template illustrating best practise docstring style.

    :param int number: A number to check.
    :returns: A boolean value
    :rtype: bool
    """
    test1 = 5 * number * number + 4
    test2 = 5 * number * number - 4
    return isPerfectSquare(test1) or isPerfectSquare(test2)


def isPerfectSquare(number: int) -> bool:
    """ Test if number is a perfect square """
    s = int(math.sqrt(number))
    return s*s == number
