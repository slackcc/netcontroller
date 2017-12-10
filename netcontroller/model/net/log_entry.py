from datetime import datetime
from pony.orm import (PrimaryKey, Optional, Required, LongStr)
from model.station import Station
from model.config import Database_Config
from .net import Net


class Log_Entry(Database_Config.db.Entity):
    id = PrimaryKey(int, auto=True)
    net = Required(Net)
    station = Required(Station)
    precedence = Optional(str)
    date_time = Required(datetime)
    remarks = Optional(LongStr)
    message_type = Optional(str)
    formal__message = Optional('Formal_Message')
