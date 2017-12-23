"""
Master class for formal messages, extended by any specific formal messages
formats.

Author: C.C. Slack
Date: 29 Nov 2017
"""

from datetime import datetime
from pony.orm import (PrimaryKey, Optional, Required, LongStr)
from model.config import DatabaseConfig
from model.net import LogEntry


class FormalMessage(DatabaseConfig.db.Entity):
    """Initialize Pony ORM model for Formal Message Table"""
    log_entry = Required(LogEntry)
    id = PrimaryKey(int, auto=True)
    date_time = Required(datetime)
    message_from = Required(str)
    message_to = Required(str)
    subject = Optional(str)
    message = Optional(LongStr)
    message_received_from = Optional('Message_Transmission',
                                     reverse='formal_message_received_from')
    message_sent_to = Optional('Message_Transmission',
                               reverse='formal_message_sent_to')
