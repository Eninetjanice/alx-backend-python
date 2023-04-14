#!/usr/bin/env python3
"""
Type-annotated func sum_mixed_list which takes a list mxd_lst of int & floats
And returns their sum as a float
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of integers and floats.
    """
    return sum(mxd_lst)
