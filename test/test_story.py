from app.parser import Parser
from app.location import Location
from app.story import Story

from pytest import mark


class MockParser:
    """Mocking Parser class."""

    def __init__(self, input_user):

        self._input_user = input_user

    def parse(self):

        return self._input_user

class MockLocation:
    def __init__(self, parser_object):

        self._input_parsed = parser_object.parse()
        self._latitude = 48.85837009999999
        self._longitude = 2.2944813

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude


def mock_requests_get(*args, **kwargs):
    """Mock requests get method.

    Return a MockResponse object.

    """

    class MockResponse:
        """Mock the Response object return by requests get method."""

        def __init__(self, **kwargs):
            self._kwargs = kwargs

        def json(self):

            result_geosearch = {
                "query": {
                    "geosearch": [{"pageid": 1359783, "title": "Tour Eiffel"}]
                }
            }

            result_extract = {
                "query": {
                    "pages": {
                        "1359783": {
                            "extract": "La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) située à Paris, à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. Son adresse officielle est 5, avenue Anatole-France.\nConstruite en deux ans par Gustave Eiffel et ses collaborateurs pour l’Exposition universelle de Paris de 1889, et initialement nommée « tour de 300 mètres », elle est devenue le symbole de la capitale française et un site touristique de premier plan : il s’agit du troisième site culturel français payant le plus visité en 2015, avec 5,9 millions de visiteurs en 2016. Depuis son ouverture au public, elle a accueilli plus de 300 millions de visiteurs.\nD’une hauteur de 312 mètres à l’origine, la tour Eiffel est restée le monument le plus élevé du monde pendant quarante ans. Le second niveau du troisième étage, appelé parfois quatrième étage, situé à 279,11 mètres, est la plus haute plateforme d'observation accessible au public de l'Union européenne et la deuxième plus haute d'Europe, derrière la tour Ostankino à Moscou culminant à 337 mètres. La hauteur de la tour a été plusieurs fois augmentée par l’installation de nombreuses antennes. Utilisée dans le passé pour de nombreuses expériences scientifiques, elle sert aujourd’hui d’émetteur de programmes radiophoniques et télévisés.\n\n"
                        }
                    }
                }
            }

            
            if self._kwargs["params"].get("list") == "geosearch":
                # Return a result for a geosearch query
                return result_geosearch
            else:
                # Return a result for an extract from wikipedia page
                return result_extract

    return MockResponse(**kwargs)


def test_mock_story_return_correct_extract_and_url(monkeypatch):

    monkeypatch.setattr("app.story.requests_get", mock_requests_get)

    mock_parser = MockParser("Tour Eiffel")

    mock_location = MockLocation(mock_parser)

    story = Story(mock_location)

    story.about()

    assert (
        story.extract
        == "La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) située à Paris, à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. Son adresse officielle est 5, avenue Anatole-France.\nConstruite en deux ans par Gustave Eiffel et ses collaborateurs pour l’Exposition universelle de Paris de 1889, et initialement nommée « tour de 300 mètres », elle est devenue le symbole de la capitale française et un site touristique de premier plan : il s’agit du troisième site culturel français payant le plus visité en 2015, avec 5,9 millions de visiteurs en 2016. Depuis son ouverture au public, elle a accueilli plus de 300 millions de visiteurs.\nD’une hauteur de 312 mètres à l’origine, la tour Eiffel est restée le monument le plus élevé du monde pendant quarante ans. Le second niveau du troisième étage, appelé parfois quatrième étage, situé à 279,11 mètres, est la plus haute plateforme d'observation accessible au public de l'Union européenne et la deuxième plus haute d'Europe, derrière la tour Ostankino à Moscou culminant à 337 mètres. La hauteur de la tour a été plusieurs fois augmentée par l’installation de nombreuses antennes. Utilisée dans le passé pour de nombreuses expériences scientifiques, elle sert aujourd’hui d’émetteur de programmes radiophoniques et télévisés.\n\n"
    )
    assert story.url == "https://fr.wikipedia.org/w/index.php?curid=1359783"


################################# Integration test

sentence_extracts_url = [
    (
        "Hello ! Qu'elle est l'adresse exacte du chateau de Guédelon ?",
        "Guédelon ou le château de Guédelon est un chantier médiéval de construction historique d'un château fort, débuté en 1997, selon les techniques et les matériaux utilisés au Moyen Âge.\nCe projet architectural situé à Treigny dans l'Yonne, dans une ancienne carrière désaffectée au centre d'une forêt et proche d'un étang, à une trentaine de kilomètres au sud-ouest d'Auxerre, vise à améliorer les connaissances en castellologie et en  archéologie expérimentale. Tout en développant une réflexion du type « art et traditions populaires », il met en scène dans un déroulement réel la construction d'un programme monumental, ce qui le différencie des parcs à thème.",
        "https://fr.wikipedia.org/w/index.php?curid=10551"
    ),
    (
        "Ah! L'horloge astronomique de Besançon, j'aimerais y retourner ! Peux-tu me pointer l'endroit sur la carte ?",
        "L'Horloge astronomique de la cathédrale Saint-Jean de Besançon est une horloge astronomique considérée comme un chef-d'œuvre du genre, construite par Auguste-Lucien Vérité au XIXe siècle. Elle fait suite à l'horloge astronomique de Constant Flavien Bernardin, construite vers 1850-1855, au fonctionnement compliqué et défectueux, disparue (ou intégrée dans celle de Vérité) vers 1860.",
        "https://fr.wikipedia.org/w/index.php?curid=945824"
    ),
    (
        "Salut ! Je voudrais toucher la Chouette de Dijon mais je n'arrive pas à la trouver. Où est-elle ?",
        "L’église Notre-Dame de Dijon, considérée comme un chef-d'œuvre d'architecture gothique du XIIIe siècle, est située au cœur des 97 hectares du secteur sauvegardé de Dijon, inscrit depuis le 4 juillet 2015 au patrimoine mondial de l'UNESCO. Elle s'élève place Notre-Dame, à proximité du Palais des ducs et des États de Bourgogne et en face de la rue Musette. On estime que l'édifice actuel a été construit des années 1220 aux années 1250 environ.\nCette église abrite la statue de Notre-Dame de Bon-Espoir, auparavant appelée Vierge noire. Elle s'orne aussi de deux symboles de la ville de Dijon : le Jacquemart et la chouette.\nL'église a été classée au titre des monuments historiques par la liste de 1840.\nLa chapelle de l'Assomption, la sacristie et la galerie les reliant à l'église sont inscrites au titre des monuments historiques depuis le 5 juillet 2002.",
        "https://fr.wikipedia.org/w/index.php?curid=1918775")
]

@mark.parametrize("input_user, extract_place, url_place", sentence_extracts_url)
def test_story_return_correct_extract_and_url_for_several_location(input_user, extract_place, url_place):


    parser = Parser(input_user)
    location = Location(parser)
    location.get_location()
    story = Story(location)

    story.about()

    assert story.extract == extract_place
    assert story.url == url_place


