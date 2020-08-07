# Simple Events - 5kyu
from collections.abc import Callable


class Event:
    """A simple event class"""

    def __init__(self):
        self._handlers = []

    def subscribe(self, function: Callable):
        """Add a function to the event's handler."""
        self._handlers.append(function)

    def unsubscribe(self, func: Callable):
        """Remove a function to the event's handler."""
        self._handlers.remove(func)

    def emit(self, *args):
        """Call all the subscribed functions with the passed arguments"""
        for func in self._handlers:
            func(*args)
