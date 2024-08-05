#!/usr/bin/env python3
"""
Provides duck-typed annotations for a function
"""
from typing import List, Optional, TypeVar

T = TypeVar('T')


def safe_first_element(lst: List[T]) -> Optional[T]:
    """
    Takes a list and returns
    """
    if lst:
        return lst[0]
    else:
        return None
