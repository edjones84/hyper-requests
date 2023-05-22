![coollogo_com-289063340](https://github.com/edjones84/hyper-requests/assets/78102381/8d7fd889-d655-432a-b048-8cbb03fe7cce)<br>
---
*Concurrent request HTTP execution library*
[![Python Package using Conda](https://github.com/edjones84/hyper-requests/actions/workflows/python-package-conda.yml/badge.svg)](https://github.com/edjones84/hyper-requests/actions/workflows/python-package-conda.yml)
## What is it?
hyper-requests is a Python library, enabling multithreading of API calls using asyncio. It takes a list of URLs and a list of parameters as input and then uses the requests library to make these calls asynchronously (https://pypi.org/project/requests/).
## Usage
### Installation
Install hyper-requests using pip:
```bash
pip install hyper-requests
```
### Example
```python
import hyper_requests

# Define the request parameters
params = [
    {'url': 'http://httpbin.org/get' , 'data': 'value1'},
    {'url': 'http://httpbin.org/get' , 'data': 'value3'},
    {'url': 'http://httpbin.org/get' , 'data': 'value5'},
    {'url': 'http://httpbin.org/get' , 'data': 'value7'},
    {'url': 'http://httpbin.org/get' , 'data': 'value9'}
]

# Create an instance of AsyncRequests and execute the requests
returned_data = hyper_requests.get(request_params=params, workers=10)

# Process the returned data
for response in returned_data:
    print(response)
```
This example demonstrates the usage of hyper-requests to perform asynchronous HTTP requests.

First, make sure you have installed hyper-requests by running the command pip install hyper-requests.

Next, import the AsyncRequests class from the hyper_requests.threader module.

Create a list of request parameters using dictionaries, where each dictionary represents a set of parameters for an individual request. In this example, each request MUST have a URL specified with the 'url' key, all other paramters must match the classic request template.

Create an instance of AsyncRequests with the request_params argument set to your list of request parameters. Specify the number of concurrent worker threads to use with the workers argument (in this case, workers=10).

Execute the requests using the run_threads() method, which returns the data obtained from the requests.

Finally, process the returned data as desired. In this example, each response is printed, but you can perform further operations based on your specific needs.
## Performance
It is hyper fast!

Within the `test/performance` directory there is a performance test that makes 20 API calls to the random joke generator api: https://official-joke-api.appspot.com/random_joke.

Using hyper requests the time taken to make these calls is ~2 second, using synchronous api calls takes ~16 seconds.

```bash
============================= test session starts ==============================
collecting ... collected 1 item

test_performance.py::PerformanceTest::test_api_performance

============================== 1 passed in 17.76s ==============================

Process finished with exit code 0
PASSED        [100%]
Asynchronous Execution time: 1.845513105392456 seconds
Asynchronous Data length: 20
Synchronous Execution time: 15.81911015510559 seconds
Synchronous Data length: 20
```
