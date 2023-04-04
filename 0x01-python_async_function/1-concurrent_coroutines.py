#!/usr/bin/env python3
"""Async routine that takes in 2 int args (in this order): n and max_delay.
Spawns wait_random n times with the specified max_delay and returns the list
of all the delays (float values) in ascending order without using sort().
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times with max_delay
    Args: n and max_delay
    Return value: Delays in ascending order.
    """
    delay_tasks = [await wait_random(max_delay) for i in range(n)]
    return sorted(delay_tasks)
