from re import sub
from app.configuration import STOPWORDS


class Parser:
    """Parse input user."""

    def __init__(self):
        """Create a parser object.

        Attribute:
            self._input_user (str): Contain a user input

        """

        self._input_user = str()

    def parse(self):
        """Parse an input user.

        Removes special characters and stop words.

        Returns:

            self._input_user (str): User input parsed

        """

        self._remove_special_characters()
        self._remove_stop_words()

        return self._input_user

    def _remove_special_characters(self):
        """Removes special characters from a sentence.

        Private method acting on self._input_user.

        """

        self._input_user = sub(r"\W", " ", self._input_user)

    def _remove_stop_words(self):
        """Removes stop words from a sentence.

        Private method acting on self._input_user.

        """

        sentence = [
            word for word in self._input_user.split() if word not in STOPWORDS
        ]

        self._input_user = "+".join(sentence)

    @property
    def input_user(self):
        return self._input_user

    @input_user.setter
    def input_user(self, input_user):
        self._input_user = str(input_user).lower()
