from app.parser import Parser
from app.location import Location
from app.unknownplaceerror import UnknownPlaceError
from pytest import fixture, mark
from pytest import raises as pytest_raises


class MockParser:
    """Mocking Parser class."""

    def __init__(self, input_user):

        self._input_user = input_user

    def parse(self):

        return self._input_user


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
                ],
                "status": "OK",
            }

            return mock_results

    return MockResponse()


def test_class_Location_can_take_a_parser_object():

    parser = MockParser("tour%20eiffel")

    place = Location(parser)

    assert place._input_parsed == "tour%20eiffel"


def test_mock_function_return_Location_of_eiffel_tower(monkeypatch):

    monkeypatch.setattr(
        "app.location.requests_get",
        mock_requests_get,
    )

    parser = MockParser("musée%20louvre")

    place = Location(parser)
    place.get_location()

    assert place.latitude, place.longitude == (
        48.85837009999999,
        2.2944813,
    )


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
    "location, coordinates",
    sentence_and_coordinates,
)
def test_Location_return_correct_Location_for_several_places(location, coordinates):

    parser = Parser(location)

    place = Location(parser)
    place.get_location()

    assert place.latitude, place.longitude == coordinates


def test_exception_catch_for_an_unknown_place():

    parser = Parser("Yop, donne moi les coordonnées du trou noir Sagittarius A*")

    place = Location(parser)

    with pytest_raises(UnknownPlaceError):
        place.get_location()
