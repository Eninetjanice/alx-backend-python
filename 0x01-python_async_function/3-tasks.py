#!/usr/bin/env python3
'''
Regular function that takes an integer max_delay and returns a asyncio.Task.
'''

import asyncio
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Any:
    """Returns an asyncio.Task that waits for a random delay."""
    return asyncio.create_task(wait_random(max_delay))
