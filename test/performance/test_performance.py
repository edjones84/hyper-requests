import time
import unittest

import requests

from src.threader import MultiThreadAPI


class PerformanceTest(unittest.TestCase):
    def test_api_performance(self):
        api_calls = 10
        request_params = [{"url": "https://official-joke-api.appspot.com/random_joke"} for _ in range(0, api_calls)]
        workers = 10  # Number of worker threads

        # run requests in async
        api = MultiThreadAPI(request_params, workers)
        start_time_async = time.time()
        data_async = api.run_api_threads()
        end_time_async = time.time()
        execution_time_async = end_time_async - start_time_async

        print(f"Concurrent Execution time: {execution_time_async} seconds")
        print(f"Concurrent Data length: {len(data_async)}")

        # run requests synchronously
        start_time_sync = time.time()
        data_sync = [requests.get(item["url"]) for item in request_params]
        end_time_sync = time.time()
        execution_time_sync = end_time_sync - start_time_sync

        print(f"Concurrent Execution time: {execution_time_sync} seconds")
        print(f"Concurrent Data length: {len(data_sync)}")

        # Assert that the results return the same values for completeness
        self.assertLess(execution_time_async, execution_time_sync)


if __name__ == '__main__':
    unittest.main()
