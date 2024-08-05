#!/usr/bin/env python3
"""
Returns a function that multiplies a float by a multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes in a float multipliers as an arg and returns function multiplier
    """
    def multiplier_function(x: float) -> float:
        """
        Return a function that multiplies a float by a multiplier
        """
        return x * multiplier
    return multiplier_function
