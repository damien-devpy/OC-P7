from app.parser import Parser


def test_parser_return_correct_string():

    parser = Parser("Bonjour ! Pourrais-je avoir la localisation de la Tour Eiffel ?")

    assert parser.parse() == "tour eiffel"

def test_parser_return_correct_string2():

    parser = Parser("Hello ! J'aurais besoin de l'adresse du Musée du Louvre.")

    assert parser.parse() == "musée louvre"

def test_parser_return_correct_string_without_preposition():

    parser = Parser("Où est la citadelle de besancon ?")

    assert parser.parse() == "citadelle besancon"

def test_parser_return_correct_string_without_preposition2():

    parser = Parser("Peux-tu chercher l'endroit où se trouve le pont du gard")

    assert parser.parse() == "pont gard"

def test_parser_return_correct_string_without_preposition3():

    parser = Parser("Dis moi, comment je me rends aux Catacombes de Paris ?")

    assert parser.parse() == "catacombes paris"