"""

This application is intended to provide a means of easily tracking checkins
and traffic in a radio net, particularly those used for emergency services
purposes.

author: C.C. Slack
version: 0.1
date: 20 Nov 2017

"""

from pony.orm import (db_session)
from model import (Address, Dbinit)

# Inital welcome screen
# Start net
#   Log checkin
# View old nets
# Print forms (CAP, ARRL, ICS)
# model.db.bind(provider='sqlite', filename='new.db', create_db=True)
# class Address(db.Entity):
#     id = PrimaryKey(int, auto=True)
#     street = Optional(str)
#     city = Optional(str)
#     state = Optional(str)
#     zip_code = Optional(str)
#     stations = Set(Station)
#     telephone = Optional(str)
#     email = Optional(str)
#     latitude = Optional(str)
#     longitude = Optional(str)
# mydb = MyDB()
# MyDB.db.generate_mapping(create_tables=True)

Dbinit()


@db_session
def create_entities():
    smb = Address(street="55 Old Billerica Rd", city="Bedford",
                  state="MA", zip_code="01730")
    return smb


addr = create_entities()
print(addr.street)
print("{}, {}".format(addr.latitude, addr.longitude))
