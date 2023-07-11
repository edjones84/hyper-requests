import unittest

import hyper_requests
from hyper_requests.threader import UnknownContent


class MyTestCase(unittest.TestCase):
    def test_xml_response(self):
        xml_dict = [
            {"url": "https://v2.jokeapi.dev/joke/Any?format=xml&contains=cat"},
            {"url": "https://v2.jokeapi.dev/joke/Any?format=xml&contains=dog"},
            {"url": "https://v2.jokeapi.dev/joke/Any?format=xml&contains=mouse"},
        ]
        response = hyper_requests.get(xml_dict)
        self.assertIsNotNone(response)

    def test_invalid_response(self):

        invalid_dict = [{"url": "https://docs.python.org/3/"}]
        with self.assertRaises(UnknownContent):
            hyper_requests.get(invalid_dict)


if __name__ == "__main__":
    unittest.main()
