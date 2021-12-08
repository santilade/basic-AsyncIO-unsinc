import asyncio
import datetime
import math
import aiohttp
import requests


def main():
    t0 = datetime.datetime.now()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    tasks = [
        # all functions are treated as async tasks

        loop.create_task(compute_some()),  # runs until is done computing, does not need await
        loop.create_task(compute_some()),  # runs until is done computing, does not need await
        loop.create_task(download_some()),  # uses api compatible with async
        loop.create_task(download_some()),  # uses api compatible with async
        loop.create_task(download_some()),  # uses api compatible with async
        loop.create_task(download_some_more()),  # uses api not compatible with async
        loop.create_task(download_some_more()),  # uses api not compatible with async
        loop.create_task(download_some_more()),  # uses api not compatible with async
        loop.create_task(wait_some()),  # runs as async task (not a fair speed comparison)
        loop.create_task(wait_some())  # runs as async task (not a fair speed comparison)
    ]

    loop.run_until_complete(asyncio.gather(*tasks))

    dt = datetime.datetime.now() - t0
    print("Asynchronous version done in {:,.2f} seconds.".format(dt.total_seconds()))


async def compute_some():
    print("Computing...")
    for i in range(1, 10 ** 7):
        math.sqrt(12345 * i)
    print("Compute done")


async def download_some():
    print("Downloading...")
    url = 'https://talkpython.fm/episodes/show/174/coming-into-python-from-another-industry-part-2'
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(url) as resp:
            resp.raise_for_status()

            text = await resp.text()

    print("Downloaded (more) {:,} characters.".format(len(text)))


async def download_some_more():
    print("Downloading more ...")
    url = 'https://pythonbytes.fm/episodes/show/92/will-your-python-be-compiled'
    resp = requests.get(url)
    resp.raise_for_status()

    text = resp.text

    print("Downloaded {:,} characters.".format(len(text)))


async def wait_some():
    print("Waiting...")
    for _ in range(1, 100):
        await asyncio.sleep(.001)


if __name__ == '__main__':
    main()
