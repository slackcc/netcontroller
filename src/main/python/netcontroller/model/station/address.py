from pony.orm import (PrimaryKey, Optional, Set)
from geopy.geocoders import Nominatim  # Import GeoCoder for lat/long
from geopy.exc import GeocoderServiceError
from ..config import DatabaseConfig
from .station import Station


class Address(DatabaseConfig.db.Entity):
    """
    Model for storing address information in the DB
    """
    geolocator = Nominatim()

    id = PrimaryKey(int, auto=True)
    street = Optional(str)
    city = Optional(str)
    state = Optional(str)
    zip_code = Optional(str)
    stations = Set(Station)
    telephone = Optional(str)
    email = Optional(str)
    latitude = Optional(float)
    longitude = Optional(float)

    def __init__(self, *args, **kwargs):
        """
        Call the original __init__ method and then populate the lat/long
        values
        """
        super(Address, self).__init__(*args, **kwargs)

        # Initialize the latitude and long for this address
        self.get_lat_long()

    @property
    def address(self):
        """
        Return the address in single line format, used primarily for
        generating the string input for the GeoCoder
        """

        return "{} {} {} {}".format(self.street,
                                    self.city,
                                    self.state,
                                    self.zip_code)

    def get_lat_long(self, update=False):
        """
        Return a tuple with latitude and longitude geocoded from the address,
        this can be used for plotting checkin locations on a map
        """

        if not (self.latitude and self.longitude) or update:
            # Only make a call to the GeoCoder if we don't already have the
            # lat_long information, or if we are forcing an update
            try:
                # The GeoCoder requires internet access, an exception will
                # occur (and is handled below) if it is not present
                location = self.geolocator.geocode(self.address)

                # @db_session
                self.latitude = location.latitude
                self.longitude = location.longitude
                DatabaseConfig.db.commit()
                return True

            except GeocoderServiceError:
                # Handle exception when no internet access by just returning
                # whatever may be already in lat_long, either nothing or the
                # old value
                return False

        # Just return the existing value by default
        return False
