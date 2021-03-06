from test.mocklocation import MockLocation
from test.mockparser import MockParser
from test.mockrequest import mock_requests_get_story

from app.story import Story


def test_mock_story_return_correct_extract_and_url(monkeypatch):

    monkeypatch.setattr("app.story.requests_get", mock_requests_get_story)

    mock_parser = MockParser("Tour Eiffel")

    mock_location = MockLocation(mock_parser)

    story = Story(mock_location)

    story.about()

    assert (
        story.extract
        == """La tour Eiffel  est une tour de fer
                            puddlé de 324 mètres de hauteur (avec antennes)
                            située à Paris, à l’extrémité nord-ouest du parc
                            du Champ-de-Mars en bordure de la Seine dans le 7e
                            arrondissement. Son adresse officielle est 5,
                            avenue Anatole-France.\nConstruite en deux ans
                            par Gustave Eiffel et ses collaborateurs pour
                            l’Exposition universelle de Paris de 1889, et
                            initialement nommée « tour de 300 mètres », elle
                            est devenue le symbole de la capitale française et
                            un site touristique de premier plan : il s’agit du
                            troisième site culturel français payant le plus
                            visité en 2015, avec 5,9 millions de visiteurs
                            en 2016. Depuis son ouverture au public, elle a
                            accueilli plus de 300 millions de visiteurs.
                            \nD’une hauteur de 312 mètres à l’origine, la
                            tour Eiffel est restée le monument le plus élevé
                            du monde pendant quarante ans. Le second niveau
                            du troisième étage, appelé parfois quatrième
                            étage, situé à 279,11 mètres, est la plus haute
                            plateforme d'observation accessible au public
                            de l'Union européenne et la deuxième plus haute
                            d'Europe, derrière la tour Ostankino à Moscou
                            culminant à 337 mètres. La hauteur de la tour
                            a été plusieurs fois augmentée par l’installation
                            de nombreuses antennes. Utilisée dans le passé
                            pour de nombreuses expériences scientifiques,
                            elle sert aujourd’hui d’émetteur de programmes
                            radiophoniques et télévisés.\n\n"""
    )

    assert story.url == "https://fr.wikipedia.org/w/index.php?curid=1359783"
