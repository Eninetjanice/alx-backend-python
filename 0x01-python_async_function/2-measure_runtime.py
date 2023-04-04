#!/usr/bin/env python3
'''
This script measures total execution time for wait_n(n, max_delay),
and returns total_time / n.
'''

import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures total execution time for wait_n(n, max_delay)
    Return value: the average time per wait
    """
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time: float = end_time - start_time
    return total_time / n
