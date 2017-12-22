from pony.orm import (PrimaryKey, Optional, Set)
from model.config import Database_Config


class Station(Database_Config.db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    callsign = Optional(str)
    address = Optional('Address')
    nets = Set('Net')
    log_entries = Set('Log_Entry')
    message_transmissions = Set('Message_Transmission')
