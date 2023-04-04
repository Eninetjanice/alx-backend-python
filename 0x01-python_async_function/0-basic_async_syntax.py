#!/usr/bin/env python3
"""
Asynchronous coroutine that takes in int arg (max_delay, default val = 10)
named wait_random that waits for random delay btw 0 & max_delay (included
and float value) seconds and eventually returns it. Using the random module
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random delay and returns it"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def main():
    """Asynchronous coroutine that runs wait_random() and prints the result"""
    delay = await wait_random()

if __name__ == "__main__":
    asyncio.run(main())
