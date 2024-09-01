#!/usr/bin/env python3
"""
Returns 10 randon numbers
"""
import asyncio
from typing import List
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers asynchronously from async_generator.
    """
    return [number for number in async_generator()]
