class MockParser:
    """Mocking Parser class."""

    def __init__(self, input_user):

        self._input_user = input_user

    def parse(self):

        return self._input_user
