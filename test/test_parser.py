from app.parser import Parser


def test_parser_return_correct_string():

    parser = Parser(
        "Salut GrandPy, donne moi l'adresse de l'Horloge Astronomique de Besançon !"
    )

    assert parser.parse() == "horloge astronomique besançon"


def test_parser_return_correct_string2():

    parser = Parser(
        "Hello ! J'aurais besoin de l'adresse du Chateau de Guédelon"
    )

    assert parser.parse() == "chateau guédelon"


def test_parser_return_correct_string_without_preposition():

    parser = Parser("Où est la citadelle de besancon ?")

    assert parser.parse() == "citadelle besancon"


def test_parser_return_correct_string_without_preposition2():

    parser = Parser(
        "Peux-tu m'indiquer où aller pour trouver le Parc des Cévènnes"
    )

    assert parser.parse() == "parc cévènnes"


def test_parser_return_correct_string_without_preposition3():

    parser = Parser("Dis moi, comment je me rends à la Place des Terreaux ?")

    assert parser.parse() == "place terreaux"


def test_parser_return_correct_string_without_verb():

    parser = Parser(
        "Hey, connais-tu la Petite Sibérie ? Pourrais-tu me donner la localisation ?"
    )

    assert parser.parse() == "petite sibérie"


def test_parser_return_correct_string_without_verb2():

    parser = Parser(
        "Je galère à trouver la Chouette de Dijon, tu peux m'aider ?"
    )

    assert parser.parse() == "chouette dijon"


def test_parser_manage_hard_sentence():

    parser = Parser("Je cherche le Louvre, où est-ce que ça se trouve ?")

    assert parser.parse() == "louvre"


def test_parser_manage_hard_sentence2():

    parser = Parser("Où se trouve l'Abbaye de Cluny ?")

    assert parser.parse() == "abbaye cluny"
