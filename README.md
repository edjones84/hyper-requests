![coollogo_com-289063340](https://github.com/edjones84/hyper-requests/assets/78102381/8d7fd889-d655-432a-b048-8cbb03fe7cce)<br>
---
*Concurrent request HTTP execution library*
[![Python Package using Conda](https://github.com/edjones84/hyper-requests/actions/workflows/python-package-conda.yml/badge.svg)](https://github.com/edjones84/hyper-requests/actions/workflows/python-package-conda.yml)
## What is it?
hyper-requests is a Python library that enables multithreading of API calls using asyncio. It takes a list of URLs and a list of parameters as input and then uses the requests library to make these calls asynchronously (https://pypi.org/project/requests/).
## Performance
It is hyper fast!

Within the `test/performance` directory there is a performance test that makes 20 API calls to the random joke generator api: https://official-joke-api.appspot.com/random_joke.

Using hyper requests the time taken to make these calls is ~2 second, using syncronous api calls takes ~16 seconds.

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
