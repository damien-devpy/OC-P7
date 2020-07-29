from app.inputuser import InputUser
from app.parser import Parser
from pytest import fixture

@fixture
def setup_parser():

    input_user = InputUser('A raw input')
    parser = Parser(input_user)

    return parser

def test_class_parser_exist(setup_parser):

    parser = setup_parser

    assert parser is not None

def test_passer_accept_a_raw_input(setup_parser):

    parser = setup_parser

    assert parser.input_object is not None

def test_parsed_input_exist(setup_parser):

    parser = setup_parser

    assert parser.input_parsed is None

def test_removing_special_characters(setup_parser):
    pass