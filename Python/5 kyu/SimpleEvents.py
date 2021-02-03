# Simple Events - 5kyu
# https://www.codewars.com/kata/52d3b68215be7c2d5300022f

# Access the link for a long task description.

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
