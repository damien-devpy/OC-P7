import re

from app.configuration import STOPWORDS


class Parser:
    """Manage and parse input user."""

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

        self._find_preposition()
        self._remove_special_characters()
        self._remove_stop_words()
        self._remove_verb_in_the_location()

        return self._input_user.strip()

    def _find_preposition(self):
        """Find preposition in a french sentence."""

        re_preposition = r" [àa]u ?.*| l[ae'] ?.*"

        sentence = re.search(re_preposition, self._input_user)

        self._input_user = (
            sentence[0] if sentence is not None else self._input_user
        )

    def _remove_special_characters(self):
        """Find and remove special characters."""

        re_special_characters = r"\W"

        self._input_user = re.sub(re_special_characters, " ", self._input_user)

    def _remove_stop_words(self):
        """Split a sentence and removes stop words."""

        string = " ".join(
            word for word in self._input_user.split() if word not in STOPWORDS
        )

        self._input_user = string

    def _remove_verb_in_the_location(self):
        """Remove verb (if exist) in the sentence."""

        re_find_verb = r"\w+(er|ir)$|\w+(er|ir) "

        self._input_user = re.sub(re_find_verb, "", self._input_user)
