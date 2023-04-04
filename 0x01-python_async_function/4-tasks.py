#!/usr/bin/env python3
'''This script executes multiple routines at the same time using async.'''

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns task_wait_random n times with max_delay
    Args: n and max_delay
    Return value: List of all delays in ascending order.
    """
    delay_tasks = [await task_wait_random(max_delay) for i in range(n)]
    return sorted(delay_tasks)
