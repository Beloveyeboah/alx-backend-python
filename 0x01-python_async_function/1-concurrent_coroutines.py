#!/usr/bin/env python3
"""
Import wait_random from the previous python file that
you’ve written and write an async
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Execute wait_random n times with
    max_delay and return list of delays """

    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
