
class InputUser:
    """Get input user."""
    
    def __init__(self, raw_input):
        """Create an input user object.

        :param raw_input: A raw input from user
        :type raw_input: str
        """
        self._raw_input = raw_input

    @property
    def raw_input(self):
        return self._raw_input