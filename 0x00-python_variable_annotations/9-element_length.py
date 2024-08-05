#!/usr/bin/env python3
"""
Annotating function parameters and return values
"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Takes in a list and returns a tuple
    """
    return [(i, len(i)) for i in lst]
