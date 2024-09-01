#!/usr/bin/env python3
"""
Measure the runtime of wait_n and calculate the average time per call.
"""

import time
from previous_module import wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Returns the average time per call.
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
