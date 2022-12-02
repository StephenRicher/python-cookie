#!/usr/bin/env python3

""" Non-public functions and classes """

import math


def isPerfectSquare(number: int) -> bool:
    """ Check if number is a perfect square. """
    s = int(math.sqrt(number))
    return s*s == number
