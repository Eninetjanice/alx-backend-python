#!/usr/bin/env python3
'''
A coroutine called async_comprehension that takes no arguments.
'''

import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous comprehension that collects 10 random ints
    and returns them as a list.
    """
    return [_ async for _ in async_generator()]
