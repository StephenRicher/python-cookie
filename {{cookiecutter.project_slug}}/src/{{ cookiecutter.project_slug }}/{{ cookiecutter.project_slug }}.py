#!/usr/bin/env python3

""" {{ cookiecutter.project_short_description }} """

import logging
import {{ cookiecutter.project_slug }}.utils as utils


logger = logging.getLogger(__name__)
{% if cookiecutter.command_line_interface|lower == 'no' %}
# Functions directly accessible from module level
__all__ = ['prime', 'fibonacci']
{% endif %}

def prime(number: int = 42) -> bool:
    """Check if a number is prime.

    This function is a template illustrating best practise docstring style.

    Args:
        number: The number to check for primality.

    Returns:
        True if prime, False otherwise.

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
    """Check if a number is part of the fibonacci sequence.

    Args:
        number: The number to check.

    Returns:
        True if in Fibonacci, False otherwise.

    """
    test1 = 5 * number * number + 4
    test2 = 5 * number * number - 4
    return utils.isPerfectSquare(test1) or utils.isPerfectSquare(test2)
