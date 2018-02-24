import logging

import requests

import settings


class API:

    def get_random_talk(self):
        logging.info("Get a random talk from the API")

        resp = requests.get(settings.VTALKS_API_RANDOM_TALK_URL)
        if resp.status_code != 200:
            logging.error("Can't fetch a random talk, response status code is", resp.status_code)
            return

        return resp.json()
