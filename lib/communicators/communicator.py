"""

Class to contain communicators who check into a net.

author: C.C. Slack
version: 0.1
date: 20 Nov 2017

"""


class Communicator():

    def __init__(self, name=None, callsign=None, address=None):
        self.name = name
        self.callsign = callsign
        self.address = address
