#!/usr/bin/env python3
"""
Adding type annotations to a function
"""
from typing import TypeVar, Dict, Optional


K = TypeVar('K')
V = TypeVar('V')


def safely_get_value(dct: Dict[K, V], key: K, default: Optional[V] = None) -> Optional[V]:
    """
    Adding appropriate type annotations
    """
    if key in dct:
        return dct[key]
    else:
        return default
