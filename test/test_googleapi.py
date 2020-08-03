from app.parser import Parser
from app.googleapi import GoogleAPI
from pytest import fixture, mark


@fixture
def setup_google_api():

    parser = MockParser()
    parser.input_user = "tour+eiffel"

    api_google = GoogleAPI(parser)

    return api_google


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


def test_class_google_api_can_take_a_parser_object(setup_google_api):

    api_google = setup_google_api
    assert api_google.input_parsed == "tour+eiffel"


def test_mock_function_return_location_of_eiffel_tower(
    setup_google_api, monkeypatch
):

    monkeypatch.setattr("app.googleapi.requests_get", mock_requests_get)

    api_google = setup_google_api
    assert api_google.location == (48.85837009999999, 2.2944813)


# Integration test

question_1 = "Bonjour ! Pourrais-je avoir la localisation de la Tour Eiffel ?"
question_2 = "quelle est l'adresse du chateau de guédelon ?"
question_3 = "Hi ! Je cherche la Citadelle de Belfort, pourrais-tu me trouver l'adresse ?"
question_4 = "Je cherche OpenClassrooms, pourrais-tu me trouver l'adresse ?"


@mark.parametrize(
    "location, coordinates",
    [
        (question_1, (48.85837009999999, 2.2944813)),
        (question_2, (47.5833887, 3.1550422)),
        (question_3, (47.636719, 6.8650283)),
        (question_4, (48.8748465, 2.3504873)),
    ],
)
def test_location_return_correct_location_for_several_places(
    location, coordinates
):

    parser = Parser()
    parser.input_user = location
    api_google = GoogleAPI(parser)

    assert api_google.location == coordinates


# from app.googleapi import GoogleAPI
# from pytest import fixture

# class MockParser:
#     """Mocking Parser class."""

#     def __init__(self):

#         self._input_user = str()

#     def parse(self):

#         return self._input_user

#     @property
#     def input_user(self):
#         return self._input_user

#     @input_user.setter
#     def input_user(self, input_user):
#         self._input_user = str(input_user)


# def test_google_api_take_a_parser_object():

#     mock_parser = MockParser()
#     mock_parser.input_user = "Tour+Eiffel"
#     api_google = GoogleAPI(mock_parser)

#     assert api_google.input_parsed == "Tour+Eiffel"

# def test_google_api_location_eiffel_tower():

#     mock_parser = MockParser()
#     mock_parser.input_user = "Tour+Eiffel"
#     api_google = GoogleAPI(mock_parser)

#     assert api_google.location == (48.85837009999999, 2.2944813)

# def test_google_api_location_louvre_museum():

#     mock_parser = MockParser()
#     mock_parser.input_user = "Musée+du+Louvre"
#     api_google = GoogleAPI(mock_parser)

#     assert api_google.location == (48.8606111, 2.337644)
