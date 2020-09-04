from app.parser import Parser
from pytest import mark

sentence_and_parsing = [
    (
        """"Salut GrandPy, donne moi l'adresse de l'Horloge Astronomique de
        Besançon !""",
        "horloge astronomique besançon",
    ),
    (
        """Hello ! J'aurais besoin de l'adresse du Chateau de Guédelon,
        merci !""",
        "chateau guédelon",
    ),
    (
        """Hi ! Je cherche la Citadelle de Belfort, pourrais-tu me trouver
        l'endroit ?""",
        "citadelle belfort",
    ),
    (
        "Où est la citadelle de besancon ?",
        "citadelle besancon",
    ),
    (
        "Peux-tu m'indiquer où aller pour trouver le Parc des Cévènnes",
        "parc cévènnes",
    ),
    (
        """Hey, connais-tu la Petite Sibérie ? Pourrais-tu me donner la
        localisation ?""",
        "petite sibérie",
    ),
    (
        "Je galère à trouver la Chouette de Dijon, tu peux m'aider ?",
        "chouette dijon",
    ),
    (
        "Dis moi, comment je me rends à la Place des Terreaux ?",
        "place terreaux",
    ),
    (
        "Où se trouve l'Abbaye de Cluny ?",
        "abbaye cluny",
    ),
    (
        "Abbaye Saint Philibert",
        "abbaye saint philibert",
    ),
    (
        "Saut du Doubs",
        "saut doubs",
    ),
    (
        "Salut granpy, peux tu me trouver la ville de Dijon ?",
        "ville dijon",
    ),
    (
        "J'aimerais avoir l'adresse de la ville de brest",
        "ville brest",
    ),
]


@mark.parametrize("sentence, sentence_parsed", sentence_and_parsing)
def test_parser_return_expected_string(sentence, sentence_parsed):

    parser = Parser(sentence)

    assert parser.parse() == sentence_parsed
