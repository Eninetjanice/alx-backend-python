#!/usr/bin/env python3
"""
Augmenting code with the correct duck-typed annotations
"""

from typing import Any, List, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a list if it exists, otherwise returns None.
    """
    if lst:
        return lst[0]
    else:
        return None
