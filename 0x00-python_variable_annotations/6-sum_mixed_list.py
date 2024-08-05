#!/usr/bin/env python3
"""
Returns the sum of an integer list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a mixed list of ints and floats and returns their sum
    """
    return float(sum(mxd_lst))
