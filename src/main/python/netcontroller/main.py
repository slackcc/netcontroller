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


Dbinit()


@db_session
def create_entities():
    smb = Address(street="2 Main Street", city="Greenfield",
                  state="MA", zip_code="01301")
    return smb


addr = create_entities()
print(addr.street)
print("{}, {}".format(addr.latitude, addr.longitude))
