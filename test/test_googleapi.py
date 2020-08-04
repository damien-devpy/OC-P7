from app.parser import Parser
from app.googleapi import GoogleAPI
from app.unknownplaceerror import UnknownPlaceError
from pytest import fixture, mark, raises


class MockParser:
    """Mocking Parser class."""

    def __init__(self):

        self._input_user = str()

    def parse(self):

        return self._input_user

    @property
    def input_user(self):
        return self._input_user

    @input_user.setter
    def input_user(self, input_user):
        self._input_user = input_user


def mock_requests_get(*args, **kwargs):
    """Mock requests get method.

    Return a MockResponse object.

    """

    class MockResponse:
        """Mock the Response object return by requests get method."""

        def __init__(self):
            pass

        def json(self):

            mock_results = {
                "results": [
                    {
                        "geometry": {
                            "location": {
                                "lat": 48.85837009999999,
                                "lng": 2.2944813,
                            }
                        }
                    }
                ]
            }

            return mock_results

    return MockResponse()


@fixture
def setup_mocking_parser():

    parser = MockParser()
    return parser


@fixture
def setup_parser():

    parser = Parser()
    return parser


def test_class_google_api_can_take_a_parser_object(setup_mocking_parser):

    parser = setup_mocking_parser
    parser.input_user = "tour+eiffel"

    api_google = GoogleAPI(parser)
    assert api_google.input_parsed == "tour+eiffel"


def test_mock_function_return_location_of_eiffel_tower(
    setup_mocking_parser, monkeypatch
):

    monkeypatch.setattr(
        "app.googleapi.requests_get", mock_requests_get,
    )

    parser = setup_mocking_parser
    parser.input_user = "musée+louvre"

    api_google = GoogleAPI(parser)
    assert api_google.location == (48.85837009999999, 2.2944813,)


############################# Integration test

sentence_and_coordinates = [
    (
        "Bonjour ! Pourrais-je avoir la localisation de le Citadelle de Besançon ?",
        (47.2318894, 6.0317377),
    ),
    (
        "Hello ! Qu'elle est l'adresse exacte du chateau de Guédelon ?",
        (47.5833887, 3.1550422),
    ),
    (
        "Hi ! Je cherche la Citadelle de Belfort, pourrais-tu me trouver l'endroit ?",
        (47.636719, 6.8650283),
    ),
    (
        "Ah! L'horloge astronomique de Besançon, j'aimerais y retourner ! Peux-tu me pointer l'endroit sur la carte ?",
        (47.23358289999999, 6.0309017),
    ),
]


@mark.parametrize(
    "location, coordinates", sentence_and_coordinates,
)
def test_location_return_correct_location_for_several_places(
    setup_parser, location, coordinates
):

    parser = setup_parser
    parser.input_user = location

    api_google = GoogleAPI(parser)
    assert api_google.location == coordinates


def test_exception_catch_for_an_unknown_place(setup_parser):

    parser = setup_parser
    parser.input_user = (
        "Yop, donne moi les coordonnées du trou noir Sagitarius A*"
    )

    api_google = GoogleAPI(parser)

    with raises(UnknownPlaceError):
        api_google.location
