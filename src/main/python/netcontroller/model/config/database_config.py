from pony.orm import Database

# from database.station import Station
# from database.net import Net
# from database.address import Address
# from database.net import Net


class Database_Config:

    db = Database(provider='sqlite', filename='new.db', create_db=True)
