#!/usr/bin/env python3
"""Async Generator"""


import asyncio
from random import randint, random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """coroutine that will loop 10 times and yield random
    between 0 and 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random() * 10
