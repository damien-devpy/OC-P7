import re
from app.configuration import STOPWORDS


class Parser:
    """Parse input user."""

    def __init__(self, input_user):
        """Create a parser object.

        Attribute:
            self._input_user (str): Contain a user input

        """

        self._input_user = input_user.lower()

    def parse(self):
        """Parse an input user.

        Returns:

            self._input_user (str): User input parsed

        """

        self._input_user = self._find_preposition()
        self._input_user = self._remove_special_characters()
        self._input_user = self._remove_stop_words()
        self._input_user = self._remove_verb_in_the_location()

        return self._input_user.strip()

    def _find_preposition(self):
        """Find preposition in a french sentence.

        And return the part after it.

        Returns:

            sentence (str): Part of the sentence after the preposition

        """
        re_preposition = r" [àa][u] ?.*| d[eu] ?.*| l[ae] ?.*"

        return re.search(re_preposition, self._input_user)[0]

    def _remove_special_characters(self):
        """Find and remove special characters."""

        re_special_characters = r"\W"

        return re.sub(re_special_characters, " ", self._input_user)

    def _remove_stop_words(self):
        """Split a sentence and removes stop words."""

        string = " ".join(
            word for word in self._input_user.split() if word not in STOPWORDS
        )

        return string

    def _remove_verb_in_the_location(self):
        """Remove verb (if exist) in the sentence."""

        re_find_verb = r"[a-zA-Z]+(er|ir|re)"

        return re.sub(re_find_verb, "", self._input_user)
