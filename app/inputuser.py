class InputUser:
    """Get input user."""

    def __init__(self, raw_input):
        """Create an input user object.

        Args:
            raw_input (str): A raw input from user

        Attribute:
            raw_input (str): Contain the raw input from user
        """
        self._raw_input = raw_input

    @property
    def raw_input(self):
        return self._raw_input
