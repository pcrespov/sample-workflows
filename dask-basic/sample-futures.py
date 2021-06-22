"""
Low-Level:

- Futures: Real-time parallel function evaluation
"""

# https://docs.dask.org/en/latest/futures.html
# https://examples.dask.org/futures.html

import random
import time
import webbrowser
from pathlib import Path

import dask.array as da
import numpy as np
from dask.distributed import Client, Future, progress
from dask.utils import is_series_like


def open_dashboard(client: Client):
    webbrowser.open(client.dashboard_link)


def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def inc(x):
    time.sleep(random.randint(1, 10))
    return x + 1


def add(x, y):
    time.sleep(random.randint(1, 10))

    return x + y


def on_done(fut: Future):
    print(fut)
    print(fut.result())


# samples


def sample_submit_task(client):
    x = client.submit(inc, 100)
    print(x)
    print(x.result())  # blocks until
    print(x)


def sample_map_tasks(client):
    xx = client.map(inc, range(100))
    print(xx)
    progress(xx)
    print([x.result() for x in xx])


def sample_dependencies(client: Client):
    x = client.submit(inc, 1)
    y = client.submit(fib, 22)
    z = client.submit(add, x, y)

    print(z.result())
    print(client.gather([x, y, z]))


def sample_submit_recursive_task(client):
    x = client.submit(fib, 100)
    print(x)
    print(x.result())  # blocks until
    print(x)


def sample_move_data(client):
    data = np.random.random(size=(100, 100))

    # Scattering moves your data to a worker and returns a future pointing to that data:
    remote_data = client.scatter(data)
    print(remote_data)

    future = client.submit(inc, remote_data)

    # Dask will spread these elements evenly throughout workers in a round-robin fashion:
    remote_data_spread = client.scatter([data, data, data])
    print(remote_data_spread)

    xx = client.map(inc, remote_data_spread)

    xx.append(future)
    res = client.gather(xx)
    print(res)


def main():
    with Client(
        asynchronous=False,
        processes=True,
        threads_per_worker=2,
        n_workers=2,
        memory_limit="1GB",
    ) as client:
        open_dashboard(client)
        # add here
        # sample_dependencies(client)
        sample_move_data(client)


if __name__ == "__main__":
    main()
