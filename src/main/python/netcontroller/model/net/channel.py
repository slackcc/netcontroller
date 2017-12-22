from pony.orm import (PrimaryKey, Optional, Set)
from model.config import DatabaseConfig


class Channel(DatabaseConfig.db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    frequency = Optional(str)
    nets = Set('Net')
