#!/usr/bin/env python3
""" Complex types - functions """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a given multiplier.
    """
    def multiplier_fn(number: float) -> float:
        return number * multiplier
    return multiplier_fn
