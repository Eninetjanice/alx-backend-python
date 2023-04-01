#!/usr/bin/env python3
"""
Adding annotation values to functions
"""

from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T', covariant=False)

def safely_get_value(dct: Mapping, key: Any, default: 
        Union[T, None] = None) -> Union[Any, T]:
    """
    Returns val of a key in a dict if it exists, else returns a default value
    """
    if key in dct:
        return dct[key]
    else:
        return default
