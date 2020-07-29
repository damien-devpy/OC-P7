class Parser:
    """Parse input user."""

    def __init__(self, input_user_object):
        """Create a parser object.

        Args:
            input_user_object (InputUser): Instance of InputUser containing a
                raw input.

        Attributes:
            input_object (InputUser): InputUser object that contain a raw input
                user.
        """

        self._input_object = input_user_object
        self._input_parsed = None

    def parse(self):
        """Parse a raw input user.

        Turn a sentence into several words that represent a place.

        """

    @property
    def input_object(self):
        return self._input_object

    @property
    def input_parsed(self):
        return self._input_parsed
    
    
