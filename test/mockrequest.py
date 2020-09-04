def mock_requests_get_location(*args, **kwargs):
    """Mock requests get method.

    Return a MockResponse object.

    """

    class MockResponse:
        """Mock the Response object return by requests get method."""

        def __init__(self):
            pass

        def json(self):

            mock_results = {
                "results": [
                    {
                        "geometry": {
                            "location": {
                                "lat": 48.85837009999999,
                                "lng": 2.2944813,
                            }
                        }
                    }
                ],
                "status": "OK",
            }

            return mock_results

    return MockResponse()


def mock_requests_get_story(*args, **kwargs):
    """Mock requests get method.

    Return a MockResponse object.

    """

    class MockResponse:
        """Mock the Response object return by requests get method."""

        def __init__(self, **kwargs):
            self._kwargs = kwargs

        def json(self):

            result_geosearch = {
                "query": {
                    "geosearch": [{"pageid": 1359783, "title": "Tour Eiffel"}]
                }
            }

            result_extract = {
                "query": {
                    "pages": {
                        "1359783": {
                            "extract": """La tour Eiffel  est une tour de fer
                            puddlé de 324 mètres de hauteur (avec antennes)
                            située à Paris, à l’extrémité nord-ouest du parc
                            du Champ-de-Mars en bordure de la Seine dans le 7e
                            arrondissement. Son adresse officielle est 5,
                            avenue Anatole-France.\nConstruite en deux ans
                            par Gustave Eiffel et ses collaborateurs pour
                            l’Exposition universelle de Paris de 1889, et
                            initialement nommée « tour de 300 mètres », elle
                            est devenue le symbole de la capitale française et
                            un site touristique de premier plan : il s’agit du
                            troisième site culturel français payant le plus
                            visité en 2015, avec 5,9 millions de visiteurs
                            en 2016. Depuis son ouverture au public, elle a
                            accueilli plus de 300 millions de visiteurs.
                            \nD’une hauteur de 312 mètres à l’origine, la
                            tour Eiffel est restée le monument le plus élevé
                            du monde pendant quarante ans. Le second niveau
                            du troisième étage, appelé parfois quatrième
                            étage, situé à 279,11 mètres, est la plus haute
                            plateforme d'observation accessible au public
                            de l'Union européenne et la deuxième plus haute
                            d'Europe, derrière la tour Ostankino à Moscou
                            culminant à 337 mètres. La hauteur de la tour
                            a été plusieurs fois augmentée par l’installation
                            de nombreuses antennes. Utilisée dans le passé
                            pour de nombreuses expériences scientifiques,
                            elle sert aujourd’hui d’émetteur de programmes
                            radiophoniques et télévisés.\n\n"""
                        }
                    }
                }
            }

            if self._kwargs["params"].get("list") == "geosearch":
                # Return a result for a geosearch query
                return result_geosearch
            else:
                # Return a result for an extract from wikipedia page
                return result_extract

    return MockResponse(**kwargs)
