from pony.orm import Database


class DatabaseConfig:

    db = Database(provider='sqlite', filename='new.db', create_db=True)
