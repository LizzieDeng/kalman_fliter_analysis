"""
A module to show off a native coroutine pipeline.

This pipe allows us to send messages back-and-forth between coroutines,
simulating what we can do with the yield statement/expression. However,
it is very arcane it shows with the native coroutines are not as useful
for animation or other modern applications.  In fact, as the name says
-- asyncio -- it really only useful for reading date from large files
or from a web server.

Author: Walker M. White
Date:   November 2, 2020
"""
import asyncio


class Pipe(object):
    """
    A class representing a communication pipe between coroutines

    This class works by having an event attribute, which works like
    a semaphore (a topic you would learn about in a 4000 level course)
    """
    # Attribute _buffer: The buffer storing the communicated data
    # Invariant: _buffer is a (possibly empty) list
    #
    # Attribute _stop: Whether to shut down this pipe permanently
    # Invariant: _stop is a boolean
    #
    # Attribute _event: The even to synchronize the two coroutines
    # Invariant: _event is a asyncio.Event()

    def __init__(self):
        """
        Initializes a new communication pipe
        """
        self._buffer = []
        self._stop = False
        self._event = asyncio.Event()

    def send(self,value):
        """
        Sends a piece of data into the pipeline buffer

        This data will then be sent to the first available coroutine
        awaiting on this pipe.

        Paramater value: The data to sent
        Precondition: NONE (value can be anything)
        """
        if not self._stop:
            self._buffer.append(value)
            self._event.set()

    def stop(self):
        """
        Stops this pipeline permanently.

        Any coroutine waiting on this pipeline will immediately
        receive None.
        """
        self._stop = True
        self._event.set()

    async def receive(self):
        """
        Returns the next bit of data in the pipe.

        This method returns a value immediately if the buffer is not
        empty. Otherwise it blocks any coroutine that awaits on it
        until the buffer is not empty
        """
        while not self._stop:
            await self._event.wait()
            self._event.clear()
            if self._stop:
                return None
            elif len(self._buffer) > 0:
                return self._buffer.pop(0)


async def helper(pipe):
    """
    A coroutine that can receive and send a message via a pipe

    Parameter pipe: The pipe to communicate
    Precondition: pipe is a Pipe object
    """
    value = await pipe.receive()
    print('Value is',value)
    pipe.send(44)


async def main():
    """
    The main, parent coroutine
    """
    p = Pipe()
    print('Creating the task')
    t = asyncio.create_task(helper(p))

    print('Sending the message')
    p.send(99)

    # Let t take over
    print('Waiting on the task')
    await t

    print('Awaiting on an answer back.')
    value = await p.receive()
    print('Value back is',value)

    # Wait for t to finsh
    print('The task is complete')


if __name__ == '__main__':
    asyncio.run(main())
