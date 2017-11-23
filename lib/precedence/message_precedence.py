"""

Extend the IntEnum class to invert the normal comparrison order so that
priority values can be logically represented.

author: C.C. Slack
version: 0.1
date: 20 Nov 2017

"""

from enum import IntEnum


class MessagePrecedence(IntEnum):

    def __gt__(self, other):
        """Invert by returning less than when greater than is called"""
        return super().__lt__(other)

    def __lt__(self, other):
        """Invert by returning greater than when less than is called"""
        return super().__gt__(other)

    def __ge__(self, other):
        """Invert by returning LT or Equal when GT or equal is called"""
        return super().__le__(other)

    def __le__(self, other):
        """Invert by returning GT or Equal when LT or Equal is called"""
        return super().__ge__(other)
