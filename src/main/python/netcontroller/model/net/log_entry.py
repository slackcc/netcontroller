from datetime import datetime
from pony.orm import (PrimaryKey, Optional, Required, LongStr)
from model.station import Station
from model.config import DatabaseConfig
from .net import Net


class LogEntry(DatabaseConfig.db.Entity):
    id = PrimaryKey(int, auto=True)
    net = Required(Net)
    station = Required(Station)
    precedence = Optional(str)
    date_time = Required(datetime)
    remarks = Optional(LongStr)
    message_type = Optional(str)
    formal__message = Optional('Formal_Message')
