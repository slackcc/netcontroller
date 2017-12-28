"""
Formal Message format for Civil Air Patrol usage, this format may be used for
both standard formal traffic on a CAPF105 form as well as coded traffic using
a CAPF105a.

Author: C.C. Slack
Date: 29 Nov 2017
"""
from pony.orm import (Optional, Required, LongStr)
from .formal_message import FormalMessage


class CAPF105Message(FormalMessage):
    """Initialize Pony ORM model for CAPF105 Messages"""
    msg_number_incoming = Optional(str)
    msg_number_outgoing = Optional(str)
    cap_precedence = Optional(str)
    info = Optional(str)
    group_count = Required(int)
    operators_notes = Optional(LongStr)
