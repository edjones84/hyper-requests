import unittest

from hyper_requests.request_builder import check_request_params


class TestCheckRequestParams(unittest.TestCase):
    def test_valid_request_parameters(self):
        request_parameters = [
            {"url": "https://example.com", "method": "GET"},
            {"url": "https://example.org", "headers": "Content-Type: application/json"},
        ]
        result = check_request_params(request_parameters)
        self.assertEqual(result, request_parameters)

    def test_invalid_request_parameters_no_matching_keys(self):
        request_parameters = [
            {"invalid_key": "value1"},
            {"invalid_key": "value2", "another_key": "value3"},
        ]
        with self.assertRaises(ValueError) as context:
            check_request_params(request_parameters)
        self.assertEqual(
            str(context.exception),
            "Invalid request parameters. No matching keys found in Request class attributes.",
        )

    def test_invalid_request_parameters_no_url_key(self):
        request_parameters = [
            {"method": "GET"},
            {"headers": "Content-Type: application/json", "body": "data"},
        ]
        with self.assertRaises(ValueError) as context:
            check_request_params(request_parameters)
        self.assertEqual(
            str(context.exception), "Invalid request parameters. No url key present"
        )


if __name__ == "__main__":
    unittest.main()
