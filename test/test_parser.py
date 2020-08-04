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

    parser = Parser("Dis moi, comment je me rends aux Catacombes de Paris ?")

    assert parser.parse() == "catacombes paris"


def test_parser_return_correct_string_without_verb():

    parser = Parser(
        "Hey, connais-tu le Pont du Gard ? Pourrais-tu me donner l'adresse ?"
    )

    assert parser.parse() == "pont gard"


def test_parser_return_correct_string_without_verb2():

    parser = Parser(
        "Je galère à trouver la Chouette de Dijon, tu peux m'aider ?"
    )

    assert parser.parse() == "chouette dijon"
