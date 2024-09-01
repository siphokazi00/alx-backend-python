#!/usr/bin/env python3
"""
Creating an asyncio.Task for the wait_random coroutine.
"""

import asyncio
from 0_basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task that runs the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
