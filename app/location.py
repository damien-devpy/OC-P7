from os import environ

from app.configuration import ENDPOINT_GOOGLE
from app.unknownplaceerror import UnknownPlaceError
from requests import get as requests_get


class Location:
    """Represent a physical location, with coordinates."""

    def __init__(self, parser_object):
        """Create a location object.

        Manage an input user that has been parsed and get his geographical
            coordinates through the Geocoding Google API.

        Args:

            parser_object (Parser): A parser object containing an input parsed

        Attribute:

            self._input_parsed (str): User input parsed
            self._latitude (float): Contain latitude coordinates for a place.
                Default to None.
            self._longitude (float): Contain longitude coordinates for a place.
                Default to None.

        """

        self._input_parsed = parser_object.parse()
        self._latitude = None
        self._longitude = None

    def get_location(self):
        """Call Google geocoding API.

        Send a parsed input, receive coordinates and set self._latitude
        and self._longitude.

        """

        params = {
            "address": self._input_parsed,
            "key": environ.get("GOOGLE_KEY"),
        }

        location = requests_get(f"{ENDPOINT_GOOGLE}", params=params).json()
        if location["status"] == "OK":
            lat = location["results"][0]["geometry"]["location"]["lat"]
            lng = location["results"][0]["geometry"]["location"]["lng"]

            self._latitude, self._longitude = lat, lng

        elif location["status"] == "ZERO_RESULTS":
            raise UnknownPlaceError

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude
