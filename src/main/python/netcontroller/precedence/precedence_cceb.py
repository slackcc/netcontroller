"""

Enumeration to reference message prededence as defined by the Combined
Communications Electronics Board, defining message precedence used by
military and CAP users.

author: C.C. Slack
version: 0.1
date: 20 Nov 2017

"""

from .message_precedence import MessagePrecedence


class PrecedenceCCEB(MessagePrecedence):
    FLASH_OVERRIDE = 0
    FLASH = 1
    IMMEDIATE = 2
    PRIORITY = 3
    ROUTINE = 4
