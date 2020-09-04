from test.mockparser import MockParser
from test.mockrequest import mock_requests_get_location

from app.location import Location


def test_class_Location_can_take_a_parser_object():

    parser = MockParser("tour%20eiffel")

    place = Location(parser)

    assert place._input_parsed == "tour%20eiffel"


def test_mock_location_return_correct_location_of_eiffel_tower(monkeypatch):

    monkeypatch.setattr(
        "app.location.requests_get",
        mock_requests_get_location,
    )

    parser = MockParser("musée%20louvre")

    place = Location(parser)
    place.get_location()

    assert place.latitude, place.longitude == (
        48.85837009999999,
        2.2944813,
    )
