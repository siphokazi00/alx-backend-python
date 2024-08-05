#!/usr/bin/env python3
"""
Using mypy to validate the following function
"""


def zoom_array(lst: Tuple[Unin[int, float], ...], factor: int = 2) -> Tuple[Union[int, float], ...]:
    """
    Uses mypy for validation
    """
    zoomed_in: Tuple[Union[int, float], ...] = tuple(
            item for item in lst
            for _ in range(factor)
    )
    return zoomed_in


array: Typle[int, ...] = (12, 72, 91)

zoom_2x = zoom_array(array)
