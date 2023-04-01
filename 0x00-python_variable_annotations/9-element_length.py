#!/usr/bin/env python3
"""
Annotating function’s pars & return vals with appropriate types
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns list of tuples containing each elem of the input list & its length
    """
    return [(i, len(i)) for i in lst]
