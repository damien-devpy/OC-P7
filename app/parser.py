import re
from app.configuration import STOPWORDS

class Parser:

    def __init__(self, input_user):

        self._input_user = str(input_user).lower()

    def parse(self):
        """Parse an input user.

        Returns:

            input_parsed (str): User input parsed

        """

        input_parsed = self._find_preposition()

        input_parsed = self._remove_special_characters(input_parsed)

        return input_parsed

    def _find_preposition(self):
        """Find preposition in a french sentence.

        And return the part after it.

        Returns:

            sentence (str): Part of the sentence after the preposition

        """
        re_preposition = r'd[eu] .*|l[ae] .*'

        sentence = re.search(re_preposition, self._input_user)[0]

        return sentence

    def _remove_special_characters(self, sentence):
        """Find and remove special characters.

        Returns:

            string (str): String without special characters

        """

        re_special_characters = r'\W'

        string = re.sub(re_special_characters, ' ', sentence).split()
        string = " ".join(word for word in string[:] if word not in STOPWORDS)

        return string