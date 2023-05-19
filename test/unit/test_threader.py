import unittest

from hyper_requests.threader import AsyncRequests


class TestThreading(unittest.TestCase):
    """Uses the overpass openstreet map api to see if two requests with different parameters can be multithreaded"""

    def setUp(self):
        self.request_params1 = [
            {
                "url": "http://overpass-api.de/api/interpreter",
                "params": {
                    "data": """[out:json];
                    ( node["amenity"=cafe](poly:"51.62909644773781 -0.7337166943001433 51.6141524997197 -0.7465585656885779 51.612491923033424 -0.7736491288733712 51.62558966499365 -0.7909261370926302 51.64180906516988 -0.7830292914980579 51.646730301488894 -0.7569629610359855 51.63597602890366 -0.7359112681284462");
                      way["amenity"=cafe](poly:"51.62909644773781 -0.7337166943001433 51.6141524997197 -0.7465585656885779 51.612491923033424 -0.7736491288733712 51.62558966499365 -0.7909261370926302 51.64180906516988 -0.7830292914980579 51.646730301488894 -0.7569629610359855 51.63597602890366 -0.7359112681284462");
                      relation["amenity"=cafe](poly:"51.62909644773781 -0.7337166943001433 51.6141524997197 -0.7465585656885779 51.612491923033424 -0.7736491288733712 51.62558966499365 -0.7909261370926302 51.64180906516988 -0.7830292914980579 51.646730301488894 -0.7569629610359855 51.63597602890366 -0.7359112681284462");
                    );
                    out center;
                    """
                },
            },
            {
                "url": "http://overpass-api.de/api/interpreter",
                "params": {
                    "data": """[out:json];
                    ( node["amenity"=school](poly:"51.62909644773781 -0.7337166943001433 51.6141524997197 -0.7465585656885779 51.612491923033424 -0.7736491288733712 51.62558966499365 -0.7909261370926302 51.64180906516988 -0.7830292914980579 51.646730301488894 -0.7569629610359855 51.63597602890366 -0.7359112681284462");
                      way["amenity"=school](poly:"51.62909644773781 -0.7337166943001433 51.6141524997197 -0.7465585656885779 51.612491923033424 -0.7736491288733712 51.62558966499365 -0.7909261370926302 51.64180906516988 -0.7830292914980579 51.646730301488894 -0.7569629610359855 51.63597602890366 -0.7359112681284462");
                      relation["amenity"=school](poly:"51.62909644773781 -0.7337166943001433 51.6141524997197 -0.7465585656885779 51.612491923033424 -0.7736491288733712 51.62558966499365 -0.7909261370926302 51.64180906516988 -0.7830292914980579 51.646730301488894 -0.7569629610359855 51.63597602890366 -0.7359112681284462");
                    );
                    out center;
                    """
                },
            },
        ]
        self.api1 = AsyncRequests(self.request_params1)

        self.request_params2 = [
            {"url": "https://official-joke-api.appspot.com/random_joke"},
            {"url": "https://official-joke-api.appspot.com/random_joke"},
        ]
        self.api2 = AsyncRequests(self.request_params2)

    def test_run_api1_threads_with_params(self):
        self.assertIsNotNone(self.api1.run_threads())

    def test_run_api2_threads_just_url(self):
        self.assertIsNotNone(self.api2.run_threads())
