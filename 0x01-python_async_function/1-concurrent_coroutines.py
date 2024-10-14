#!/usr/bin/env python3

"""
mport wait_random from the previous python file that
you’ve written and write an async
"""


from 0-basic_async_syntax import wait_random
import asyncio
import heapq


async def wait_n(n: int, max_delay: int) -> list:
    """ async """

    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return list(heapq.merge(*[sorted([delay]) for delay in delays]))
