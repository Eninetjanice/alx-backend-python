#!/usr/bin/env python3
'''
Coroutine that takes no arguments, loops 10x while waiting time asynchronously
for 1 second, and yields a random number between 0 and 10.
'''

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''A coreroutine that takes no argument & yields randomly btw 0 & 10'''
    for i in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
