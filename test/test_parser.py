from app.parser import Parser
from pytest import fixture


@fixture
def setup_parser():

    parser = Parser()

    return parser


def test_parser_taking_an_input(setup_parser):

    parser = setup_parser

    parser.input_user = "This is an input made by an user"

    assert parser.input_user == "this is an input made by an user"


def test_parser_removes_special_character(setup_parser):

    parser = setup_parser

    parser.input_user = "#@*$%*"

    string_without_spec_char = parser.parse()

    assert string_without_spec_char == ""


def test_parser_dont_removes_letters(setup_parser):

    parser = setup_parser

    parser.input_user = "#@*$%*musée"

    string_without_spec_char = parser.parse()

    assert string_without_spec_char == "musée"


def test_parser_manage_numbers(setup_parser):

    parser = setup_parser

    parser.input_user = 42

    string_parsed = parser.parse()

    assert string_parsed == "42"


def test_parser_removes_stop_words(setup_parser):

    parser = setup_parser

    parser.input_user = "Bonjour, je tu il nous vous ils"

    string_without_stop_words = parser.parse()

    assert string_without_stop_words == ""


def test_parser_still_removes_stop_words(setup_parser):

    parser = setup_parser

    parser.input_user = "ils Nous Aurait Vous Ils Dans"

    string_without_stop_words = parser.parse()

    assert string_without_stop_words == ""


def test_parser_removes_spec_char_and_stop_words(setup_parser):

    parser = setup_parser

    parser.input_user = (
        "Bonjour, je voudrais la localisation de la Tour Eiffel !"
    )

    string_parsed = parser.parse()

    assert string_parsed == "tour+eiffel"


def test_parser_another_sentence(setup_parser):

    parser = setup_parser

    parser.input_user = "Quelle est l'adresse du Chateau de Guédelon ?"

    string_parsed = parser.parse()

    assert string_parsed == "chateau+guédelon"


def test_parser_another_sentence_2(setup_parser):

    parser = setup_parser

    parser.input_user = (
        "Hello ! J'aurais besoin de l'adresse du Musée du Louvre."
    )

    string_parsed = parser.parse()

    assert string_parsed == "musée+louvre"
