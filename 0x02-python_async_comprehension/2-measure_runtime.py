#!/usr/bin/env python3
'''
Coroutine that execute async_comprehension 4x in parallel using asyncio.gather
The measure_runtime function measures the total runtime and returns it.
'''

import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Measures total runtime and returns it as an array'''
    start_time: float = time.perf_counter()
    task: list = [asyncio.create_task(async_comprehension()) for i in range(4)]
    result: list = await asyncio.gather(*task)
    end_time: float = time.perf_counter()
    total_time: float = end_time - start_time
    return total_time
