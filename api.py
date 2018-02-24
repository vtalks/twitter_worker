import logging

import requests


def get_random_talk():
    logging.debug("Get a random talk ...")

    r = requests.get('https://vtalks.net/api/random-talk/')
    if r.status_code != 200:
        logging.error("Can't fetch a random talk, response status code is", r.status_code)
        return

    return r.json()