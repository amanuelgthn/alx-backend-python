#!/usr/bin/env python3
"""Basics of Python"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ An asynchronous coroutine that takes an intergr nad returns
    the value it waited"""
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
