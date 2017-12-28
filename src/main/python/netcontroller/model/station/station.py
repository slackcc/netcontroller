from pony.orm import (PrimaryKey, Optional, Set)
from ..config import DatabaseConfig


class Station(DatabaseConfig.db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    callsign = Optional(str)
    address = Optional('Address')
    nets = Set('Net')
    log_entries = Set('Log_Entry')
    message_transmissions = Set('Message_Transmission')
