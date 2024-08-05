#!/usr/bin/env python3
"""
Takes variables of different types and returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and an int or float as args and returns a tuple
    """
    return (k, floar(v ** 2))
