"""

This application is intended to provide a means of easily tracking checkins
and traffic in a radio net, particularly those used for emergency services
purposes.

author: C.C. Slack
version: 0.1
date: 20 Nov 2017

"""

from lib.communicators.address import Address

# Inital welcome screen
# Start net
#   Log checkin
# View old nets
# Print forms (CAP, ARRL, ICS)

addr = Address("55 Old Billerica Rd", "Bedford", "MA", "01730")
print(addr.lat_long)
