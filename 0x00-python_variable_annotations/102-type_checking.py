#!/usr/bin/env python3
"""
Validating code with mypy and applying changes
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Return necessary changes """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
        ]
    return zoomed_in


array: Tuple[int, int, int] = (12, 72, 91)

zoom_2x: Tuple[int, ...] = zoom_array(array)

zoom_3x: Tuple[int, ...] = zoom_array(array, 3)
