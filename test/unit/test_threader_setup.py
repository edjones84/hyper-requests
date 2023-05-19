import unittest
from unittest.mock import MagicMock

import requests

from hyper_requests.threader import AsyncRequests


class TestThreadingSetup(unittest.TestCase):
    def setUp(self):
        self.request_params = [
            {"url": "https://api.example.com/endpoint1", "param": "value1"},
            {"url": "https://api.example.com/endpoint2", "param": "value2"},
        ]
        self.api = AsyncRequests(self.request_params)

    def test_init(self):
        self.assertEqual(self.api.request_params, self.request_params)
        self.assertEqual(self.api.workers, 10)

    def test__fetch(self):
        session = MagicMock(spec=requests.Session)
        response = MagicMock()
        response.json.return_value = {"key": "value"}
        session.get.return_value.__enter__.return_value = response

        data = self.api._fetch(
            session, {"url": "https://api.example.com/endpoint", "param": "value"}
        )

        session.get.assert_called_once_with(
            url="https://api.example.com/endpoint", param="value"
        )
        response.json.assert_called_once()
        self.assertEqual(data, {"key": "value"})


if __name__ == "__main__":
    unittest.main()
