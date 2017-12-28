from pony.orm import (PrimaryKey, Optional, Set)
from model.config import Database_Config


class Channel(Database_Config.db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    frequency = Optional(str)

    nets = Set('Net')
