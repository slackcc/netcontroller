"""
Defines the model for recording who sent formal messages and when.

Author: C.C. Slack
Date: 29 Nov 2017
"""

from datetime import datetime
from pony.orm import (PrimaryKey, Required, Optional)
from model.config import DatabaseConfig
from model.station import Station
from .formal_message import FormalMessage


class MessageTransmission(DatabaseConfig.db.Entity):
    """Initialize Pony ORM for message transmission table"""
    id = PrimaryKey(int, auto=True)
    station = Required(Station)
    date_time = Optional(datetime)
    formal_message_received_from = Optional(FormalMessage,
                                            reverse='message_received_from')
    formal_message_sent_to = Optional(Formal_Message,
                                      reverse='message_sent_to')
