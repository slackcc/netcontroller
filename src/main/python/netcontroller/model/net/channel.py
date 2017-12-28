from pony.orm import (PrimaryKey, Optional, Set)
from ..config import DatabaseConfig


class Channel(DatabaseConfig.db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    frequency = Optional(str)

    nets = Set('Net')
