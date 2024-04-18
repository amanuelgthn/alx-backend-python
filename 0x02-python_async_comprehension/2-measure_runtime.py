#!/usr/bin/env python3
"""Run time for four parallel comprehension"""


import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    corouting that execures async funciton in parallel
    and measures runtime execution
    """
    time.start_time = time.time()
    await asyncio.gather(async_comprehension())
    time.end_time = time.time()
    return time.end_time - time.start_time
