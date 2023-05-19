import asyncio
from concurrent.futures import ThreadPoolExecutor

import nest_asyncio
import requests

from hyper_requests.request_builder import check_request_params

nest_asyncio.apply()


class AsyncRequests:
    """Using asyncio this allows for multithreading of API calls. Pass in a list of URLs and a list of parameters."""

    def __init__(self, request_params: list[dict[str, str]], workers: int = 10):
        self.request_params = check_request_params(request_params)
        self.workers = workers

    @staticmethod
    def _fetch(session, dict_in: dict[str, str]):
        """Private method that runs the request to the API and returns the JSON data"""
        with session.get(**dict_in) as response:
            data = response.json()
            return data

    async def _get_data_asynchronous(self):
        """Implements the multithreading"""

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

    def run_threads(self):
        """Implements the loop that multithreads and outputs data"""
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(self._get_data_asynchronous())
        loop.run_until_complete(future)
        data = future.result()
        return data
