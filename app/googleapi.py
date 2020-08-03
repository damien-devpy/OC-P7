from os import environ
from requests import get as requests_get
from app.configuration import ENDPOINT_GOOGLE
from app.unknownplaceerror import UnknownPlaceError


class GoogleAPI:
    """Manage Google API."""

    def __init__(self, parser_object):
        """Create an object calling for the API.

        Args:

            parser_object (Parser): A parser object containing an input parsed

        Attribute:

            self._input_parsed (str): User input parsed

        """

        self._input_parsed = parser_object.parse()

    def _location(self):
        """Call Google geocoding API.

        Send a parsed input and receive coordinates.

        Returns:

            coordinates (tuple): Pair of float coordinates like (latitude, longitude)

        """

        params = {
            "address": self._input_parsed,
            "key": environ.get("GOOGLE_KEY"),
        }

        location = requests_get(f"{ENDPOINT_GOOGLE}", params=params).json()

        try:
            lat = location["results"][0]["geometry"]["location"]["lat"]
            lng = location["results"][0]["geometry"]["location"]["lng"]
        except IndexError as err:
            raise UnknownPlaceError

        return lat, lng

    @property
    def input_parsed(self):
        return self._input_parsed

    @property
    def location(self):
        return self._location()
