"""
Formal Message format for the Incident Command System using form ICS213.

Author: C.C. Slack
Date: 29 Nov 2017
"""

from datetime import datetime
from pony.orm import (Optional, LongStr)
from .formal_message import FormalMessage


class ICS213Message(FormalMessage):
    """Initialize Pony ORM for ICS213 Message table"""
    to_position = Optional(str)
    from_position = Optional(str)
    message_position = Optional(str)
    reply = Optional(LongStr)
    reply_date_time = Optional(datetime)
    reply_position = Optional(str)
    message_signature = Optional(str)
    reply_signature = Optional(str)
