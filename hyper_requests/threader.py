"""
hyper-requests

A package that provides asynchronous and multithreaded API request functionality using asyncio and requests.

Usage:
- Import the package: `import hyper_requests`
- Use the `get` function to fetch data from multiple URLs asynchronously: `hyper_requests.get(request_params, workers)`

The `get` function accepts a list of dictionaries containing URL and parameter information. It performs asynchronous
requests using multithreading, allowing for efficient retrieval of data from multiple APIs concurrently.

The `check_request_params` function is provided for validating the request parameters, ensuring that they match the
attributes of the `Request` class from the `requests` library.

For more information and examples, refer to the documentation.

:copyright: (c) 2023 by Ed Jones.
:license: MIT, see LICENSE for more details.
"""

import asyncio
from concurrent.futures import ThreadPoolExecutor
from typing import Any

import nest_asyncio
import requests

from hyper_requests.request_builder import check_request_params

nest_asyncio.apply()


def get(
    request_params: list[dict[str, Any]], workers: int = 10
) -> list[dict[str, Any]]:
    """
    Fetches data from multiple URLs asynchronously using multithreading.

    :param request_params: List of dictionaries containing URL and parameter information.
    :param workers: Number of concurrent workers to use for multithreading. Default is 10.
    :return: List of JSON data returned by the APIs.
    """
    with AsyncRequests(request_params, workers) as requester:
        return requester.run_threads()


class AsyncRequests:
    """Using asyncio this allows for multithreading of API calls. Pass in a list of URLs and a list of parameters."""

    def __init__(self, request_params: list[dict[str, Any]], workers: int = 10):
        """
        Initializes the AsyncRequests class.

        :param request_params: List of dictionaries containing URL and parameter information.
        :param workers: Number of concurrent workers to use for multithreading. Default is 10.
        """
        self.request_params = check_request_params(request_params)
        self.workers = workers

    def __enter__(self):
        """Enter the context."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the context.

        :param exc_type: Exception type (if an exception occurred) or None (if no exception occurred).
        :param exc_val: Exception value (instance of the exception that was raised) or None.
        :param exc_tb: Exception traceback object (contains information about the stack frames) or None.
        """
        pass

    @staticmethod
    def _fetch(session, dict_in: dict[str, str]) -> dict[str, Any]:
        """
        Private method that runs the request to the API and returns the JSON data.

        :param session: The requests session object.
        :param dict_in: Dictionary containing the request parameters (URL, headers, etc.).
        :return: JSON data returned by the API.
        """
        with session.get(**dict_in) as response:
            content_type = response.headers["Content-Type"]
            print(content_type)
            if "json" in content_type:
                data = response.json()
            elif "xml" in content_type:
                data = response.text
            else:
                raise UnknownContent("Response type is not valid")
            return data

    async def _get_data_asynchronous(self) -> list[dict[str, Any]]:
        """
        Implements the multithreading to fetch data from multiple URLs asynchronously.

        :return: List of JSON data returned by the APIs.
        """
        with ThreadPoolExecutor(max_workers=self.workers) as executor:
            with requests.Session() as session:
                # Set any session parameters here before calling `fetch`

                # Initialize the event loop
                loop = asyncio.get_event_loop()

                # Use list comprehension to create a list of tasks to complete.
                # The executor will run the `fetch` function for each URL and its corresponding parameter
                tasks = [
                    loop.run_in_executor(
                        executor,
                        self._fetch,
                        *(
                            session,
                            dictionary,
                        )
                    )
                    for dictionary in self.request_params
                ]

                # Initializes the tasks to run and awaits their results
                json_data = [response for response in await asyncio.gather(*tasks)]
        return json_data

    def run_threads(self) -> list[dict[str, Any]]:
        """
        Implements the loop that multithreads and outputs data.

        :return: List of JSON data returned by the APIs.
        """
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(self._get_data_asynchronous())
        loop.run_until_complete(future)
        data = future.result()
        return data


class UnknownContent(Exception):
    """Unknown content type exception"""

    pass
