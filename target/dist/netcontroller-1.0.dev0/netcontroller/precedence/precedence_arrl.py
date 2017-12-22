"""

Enumeration to reference message prededence as defined by the American
Radio Relay League, used primarily by Amateur Radio opertors passing ARRL
radiogram traffic.

author: C.C. Slack
version: 0.1
date: 20 Nov 2017

"""

from .message_precedence import MessagePrecedence


class PrecedenceARRL(MessagePrecedence):
    EMERGENCY = 0
    PRIORITY = 1
    WELFARE = 2
    ROUTINE = 3
