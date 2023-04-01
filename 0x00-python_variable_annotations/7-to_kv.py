#!/usr/bin/env python3
"""
Func to_kv that takes a str k & an int OR float v as args and returns a tuple.
The first element of the tuple is the string k.
The second element is the square of the int/float v & annotated as a float.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns tuple containing a str k & the square of an int/float v as a float
    """
    return (k, v ** 2)
