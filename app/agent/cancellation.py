import asyncio

class CancellationToken:
    def __init__(self):
        self.event = asyncio.Event()

    def cancel(self):
        self.event.set()

    def reset(self):
        self.event.clear()

    @property
    def cancelled(self):
        return self.event.is_set()
