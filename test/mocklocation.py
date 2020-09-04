class MockLocation:
    def __init__(self, parser_object):

        self._input_parsed = parser_object.parse()
        self._latitude = 48.85837009999999
        self._longitude = 2.2944813

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude
