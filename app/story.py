from app.configuration import (
    ENDPOINT_WIKIMEDIA,
    URL_WIKIPEDIA,
    PARAMS_GEOSEARCH,
    PARAMS_EXTRACT,
)
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
        """Calling for the Wikimedia API."""

        page_id, page_title = self._get_url()
        self._get_extract(page_id, page_title)

    def _get_url(self):
        """Set url for the wikipedia page of the given location."""

        PARAMS_GEOSEARCH["gscoord"] = f"{self._latitude}|{self._longitude}"

        wiki_page = requests_get(
            f"{ENDPOINT_WIKIMEDIA}", params=PARAMS_GEOSEARCH
        ).json()

        page_id, page_title = (
            wiki_page["query"]["geosearch"][0]["pageid"],
            wiki_page["query"]["geosearch"][0]["title"].replace(" ", "_"),
        )

        self._url = URL_WIKIPEDIA + str(page_id)

        return page_id, page_title

    def _get_extract(self, page_id, page_title):
        """Get an extract from a wikipedia page of the given location."""

        PARAMS_EXTRACT["titles"] = f"{page_title}"

        extract = requests_get(f"{ENDPOINT_WIKIMEDIA}", params=PARAMS_EXTRACT).json()

        self._extract = extract["query"]["pages"][f"{page_id}"]["extract"]

    @property
    def extract(self):
        return self._extract

    @property
    def url(self):
        return self._url
