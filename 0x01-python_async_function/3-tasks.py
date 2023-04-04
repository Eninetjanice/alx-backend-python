#!/usr/bin/env python3
'''
Regular function that takes an integer max_delay and returns a asyncio.Task.
'''

import asyncio
from asyncio.tasks import Task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """Returns an asyncio.Task that waits for a random delay."""
    return asyncio.create_task(wait_random(max_delay))
