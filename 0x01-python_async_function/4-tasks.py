#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """an async routine that takes 2 arguments and returns
    a list of all delays"""
    tasks = [task_wait_random(max_delay) for i in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
