#!/usr/bin/env python3

"""

Write a coroutine called async_generator that takes no arguments.
"""


import asyncio
import random


async def async_generator():
    """ async
    """

    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)
