#!/usr/bin/env python3

"""
Take the code from wait_n and alter it into a new function
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run task_wait_random n times with a maximum delay of max_delay
    and return a list of the resulting delays in ascending order.
    """
    # Create a list to hold the task objects
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    # Gather all the tasks and wait for them to complete
    delays = await asyncio.gather(*tasks)

    # Sort the list of delays before returning
    return sorted(delays)
