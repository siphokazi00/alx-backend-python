#!/usr/bin/env python3
"""
Spawns wait_random and returns the delays in ascending order.
"""

import asyncio
from typing import List
from previous_module import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns the list of all the delays in ascending order.
    """
    delays = []
    for _ in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))

    completed_delays = []
    for delay in asyncio.as_completed(delays):
        completed_delays.append(await delay)

    return completed_delays
