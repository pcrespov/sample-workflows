"""
Low-Level:

- Futures: Real-time parallel function evaluation
"""

# https://docs.dask.org/en/latest/futures.html
# https://examples.dask.org/futures.html

import random
import time
import webbrowser

from dask.distributed import Client, Future, progress


def open_dashboard(client: Client):
    webbrowser.open_new_tab(client.dashboard_link)


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


def sample_submit_recursive_task(client):
    x = client.submit(fib, 100)
    print(x)
    print(x.result())  # blocks until
    print(x)


if __name__ == "__main__":
    client = Client()
    open_dashboard(client)
    sample_submit_task(client)
    client.close()
