from pony.orm import (PrimaryKey, Optional, Set, Required)
from datetime import datetime
from ..station import Station
from ..config import DatabaseConfig
from .channel import Channel


class Net(DatabaseConfig.db.Entity):
    id = PrimaryKey(int, auto=True)
    channels = Set(Channel)
    net_opened = Optional(datetime)
    net_closed = Optional(datetime)
    net_type = Optional(str)
    name = Required(str)
    log_entries = Set('Log_Entry')
    net_control = Required(Station)
