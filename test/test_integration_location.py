from app.location import Location
from app.parser import Parser
from app.unknownplaceerror import UnknownPlaceError
from pytest import mark
from pytest import raises as pytest_raises

sentence_and_coordinates = [
    (
        """Bonjour ! Pourrais-je avoir la localisation de le Citadelle de
        Besançon ?""",
        (47.2318894, 6.0317377),
    ),
    (
        "Hello ! Qu'elle est l'adresse exacte du chateau de Guédelon ?",
        (47.5833887, 3.1550422),
    ),
    (
        """Hi ! Je cherche la Citadelle de Belfort, pourrais-tu me trouver
        l'endroit ?""",
        (47.636719, 6.8650283),
    ),
    (
        """Ah! L'horloge astronomique de Besançon, j'aimerais y retourner !
        Peux-tu me pointer l'endroit sur la carte ?""",
        (47.23358289999999, 6.0309017),
    ),
]


@mark.parametrize(
    "location, coordinates",
    sentence_and_coordinates,
)
def test_Location_return_correct_Location_for_several_places(
    location, coordinates
):

    parser = Parser(location)

    place = Location(parser)
    place.get_location()

    assert place.latitude, place.longitude == coordinates


def test_exception_catch_for_an_unknown_place():

    parser = Parser(
        "Yop, donne moi les coordonnées du trou noir Sagittarius A*"
    )

    place = Location(parser)

    with pytest_raises(UnknownPlaceError):
        place.get_location()
