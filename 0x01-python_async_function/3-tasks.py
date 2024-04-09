#!/usr/bin/env python3
"""Tasks"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    function that takes an integer and returns asyncio.Task
    """
    task = asyncio.Task(wait_random(max_delay))
    return task
