#!/usr/bin/env python3
"""
Measures total runtime and returns it.
"""
import asyncio
from time import time
from your_module import async_comprehension


async def measure_runtime() -> float:
    """
    Measures total runtime and returns it.
    """
    start_time = time()
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    end_time = time()
    return end_time - start_time
