"""
A module to show off a simple native coroutine pipeline.

The main coroutine is run with asyncio.run.  All others are tasks with
asyncio.create_task

Author: Walker M. White
Date:   November 2, 2020
"""
import asyncio


async def helper(n):
    """
    A coroutine that prints out 'Hello Word!' n times

    Parameter n: The number of times to print
    Precondition: n is an int > 0
    """
    for x in range(n):
        print('Hello World!')


async def main():
    """
    The main, parent coroutine
    """
    print('Creating the task')
    t = asyncio.create_task(helper(5))

    # Let t take over
    print('Waiting on the task')
    await t

    # Wait for t to finsh
    print('The task is complete')


if __name__ == '__main__':
    asyncio.run(main())
