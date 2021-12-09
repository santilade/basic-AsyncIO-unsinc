import datetime
import math
import time
import requests


def main():
    t0 = datetime.datetime.now()

    compute_some()  # this will run first
    compute_some()  # then this
    download_some()  # then this
    download_some()  # then this
    download_some()  # then this
    download_some_more()  # then this
    download_some_more()  # then this
    download_some_more()  # then this
    wait_some()  # then this
    wait_some()  # then this

    dt = datetime.datetime.now() - t0
    print("Done in {:,.2f} seconds.".format(dt.total_seconds()))


def compute_some():
    print("Computing...")
    for i in range(1, 10 ** 7):
        math.sqrt(12345 * i)
    print("Compute done")


def download_some():
    print("Downloading...")
    url = 'https://talkpython.fm/episodes/show/174/coming-into-python-from-another-industry-part-2'
    resp = requests.get(url)
    resp.raise_for_status()

    text = resp.text

    print("Downloaded {:,} characters.".format(len(text)))


def download_some_more():
    print("Downloading more ...")
    url = 'https://pythonbytes.fm/episodes/show/92/will-your-python-be-compiled'
    resp = requests.get(url)
    resp.raise_for_status()

    text = resp.text

    print("Downloaded {:,} characters (more).".format(len(text)))


def wait_some():
    print("Waiting...")
    for _ in range(1, 100):
        time.sleep(.001)


if __name__ == '__main__':
    main()
