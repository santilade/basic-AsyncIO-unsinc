import asyncio
import datetime
import math
from unsync import unsync
import aiohttp
import requests


def main():
    t0 = datetime.datetime.now()

    tasks = [
        compute_some(),  # runs on multiprocessing
        compute_some(),  # runs on multiprocessing
        download_some(),  # runs as async task
        download_some(),  # runs as async task
        download_some(),  # runs as async task
        download_some_more(),  # runs on a thread
        download_some_more(),  # runs on a thread
        download_some_more(),  # runs on a thread
        wait_some(),  # runs as async task
        wait_some()  # runs as async task
    ]

    for t in tasks:
        t.result()

    dt = datetime.datetime.now() - t0
    print("Unsync version done in {:,.2f} seconds.".format(dt.total_seconds()))


@unsync(cpu_bound=True)
def compute_some():
    print("Computing...")
    for i in range(1, 10 ** 7):
        math.sqrt(12345 * i)
    print("Compute done")


@unsync
async def download_some():
    print("Downloading...")
    url = 'https://talkpython.fm/episodes/show/174/coming-into-python-from-another-industry-part-2'
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(url) as resp:
            resp.raise_for_status()

            text = await resp.text()

    print("Downloaded (more) {:,} characters.".format(len(text)))


@unsync
def download_some_more():
    print("Downloading more ...")
    url = 'https://pythonbytes.fm/episodes/show/92/will-your-python-be-compiled'
    resp = requests.get(url)
    resp.raise_for_status()

    text = resp.text

    print("Downloaded {:,} characters.".format(len(text)))


@unsync
async def wait_some():
    print("Waiting...")
    for _ in range(1, 100):
        await asyncio.sleep(.001)


if __name__ == '__main__':
    main()
