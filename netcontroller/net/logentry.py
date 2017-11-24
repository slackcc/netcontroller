"""Class to describe log entries"""

import datetime


class LogEntry:

    def __init__(self, callsign=None, channel=None, traffic=None,
                 remarks=None, message=None):
        """Initialize class"""
        self.time = datetime.datetime.now()
        self.callsign = callsign
        self.channel = channel
        self.traffic = traffic
        self.remarks = remarks
        self.message = message
