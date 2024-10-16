#!/usr/bin/env python3

"""
measure_runtime should measure the total runtime and return it.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of running async_comprehension four times in parallel.
    """

    start_time = time.perf_counter()  # Start the timer
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = time.perf_counter()  # End the timer
    return end_time - start_time
