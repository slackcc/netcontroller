"""
Formal Message format for the ARRL Radiogram message used by amateur Radio
operators for passing formal traffic

Author: C.C. Slack
Date: 29 Nov 2017
"""

from datetime import datetime
from pony.orm import Optional
from .formal_message import Formal_Message


class ARRL_Radiogram(Formal_Message):
    """Initialize Pony ORM model for ARRL Radiograms"""
    number = Optional(str)
    arrl_precedence = Optional(str)
    hx = Optional(str)
    check = Optional(str)
    place_of_origin = Optional(str)
    date_time_filed = Optional(datetime)
    to_email = Optional(str)
    to_phone = Optional(str)
