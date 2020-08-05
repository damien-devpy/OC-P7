from app.configuration import ENDPOINT_WIKIMEDIA, URL_WIKIPEDIA
from requests import get as requests_get

class Story:
    """Represent story about a physical place."""

    def __init__(self, location_object):
        """Create a story object. 

        Contain coordinates, story and url to the location.

        Args:

            location_object (Location): Location object containing coordinates
                of a place for recovering story

        Attributes:

            self._latitude (float): latitude of the location
            self._longitude (float): longitude of the location

            self._extract (str): Extract intro from page of the location.
                Default to None.
            self._url (str): Url to the wikpedia page location.
                Default to None.

        """
        self._latitude = location_object.latitude
        self._longitude = location_object.longitude

        self._extract = None
        self._url = None

    def about(self):
        """Calling for the Wikimedia API.

        Get an extract intro from page of the given location and set his url.

        """

        params_geosearch = {
            "action": "query",
            "list": "geosearch",
            "gscoord": f"{self._latitude}|{self._longitude}",
            "format": "json",
        }

        wiki_page = requests_get(
            f"{ENDPOINT_WIKIMEDIA}", params=params_geosearch
        ).json()

        page_id, page_title = (
            wiki_page["query"]["geosearch"][0]["pageid"],
            wiki_page["query"]["geosearch"][0]["title"].replace(" ", "_"),
        )

        self._url = URL_WIKIPEDIA + str(page_id)

        params_extract = {
            "action": "query",
            "prop": "extracts",
            "exintro": "True",
            "explaintext": "True",
            "titles": f"{page_title}",
            "format": "json",
        }

        extract = requests_get(
            f"{ENDPOINT_WIKIMEDIA}", params=params_extract
        ).json()

        self._extract = extract["query"]["pages"][f"{page_id}"]["extract"]

    @property
    def extract(self):
        return self._extract

    @property
    def url(self):
        return self._url
