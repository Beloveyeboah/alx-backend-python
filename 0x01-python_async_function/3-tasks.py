#!/usr/bin/env python3

"""

Write a function (do not create an async function,
use the regular function syntax to do this)
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Create and return an asyncio.Task """
    return asyncio.create_task(wait_random(max_delay))
