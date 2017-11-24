"""

Class to contain physical address of communicators

author: C.C. Slack
version: 0.1
date: 20 Nov 2017

"""
from geopy.geocoders import Nominatim  # Import GeoCoder for lat/long
from geopy.exc import GeocoderServiceError


class Address:

    geolocator = Nominatim()

    def __init__(self,
                 street_address="",
                 city="",
                 state="",
                 zip_code=""):
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.lat_long = None  # Set to none initially

        self.lat_long = self.get_lat_long()

    def address(self):
        """
        Return the address in single line format, used primarily for
        generating the string input for the GeoCoder
        """

        return "{} {} {} {}".format(self.street_address,
                                    self.city,
                                    self.state,
                                    self.zip_code)

    def get_lat_long(self, update=False):
        """
        Return a tuple with latitude and longitude geocoded from the address,
        this can be used for plotting checkin locations on a map
        """

        if self.lat_long is None or update:
            # Only make a call to the GeoCoder if we don't already have the
            # lat_long information, or if we are forcing an update
            try:
                # The GeoCoder requires internet access, an exception will
                # occur (and is handled below) if it is not present
                location = self.geolocator.geocode(self.address())
                return (location.latitude, location.longitude)
            except GeocoderServiceError:
                # Handle exception when no internet access by just returning
                # whatever may be already in lat_long, either nothing or the
                # old value
                return self.lat_long

        # Just return the existing value by default
        return self.lat_long
