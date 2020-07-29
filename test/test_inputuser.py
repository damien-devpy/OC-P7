from pytest import fixture
from app.inputuser import InputUser


@fixture
def setup_input_user():

    input_user = InputUser("This is an input")
    return input_user


def test_input_user_exist(setup_input_user):

    input_user = setup_input_user
    assert input_user is not None


def test_input_user_contain_raw_input(setup_input_user):

    input_user = setup_input_user
    assert input_user.raw_input == "This is an input"
