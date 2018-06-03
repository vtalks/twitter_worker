import logging

import requests

import settings


class API:

    def get_version(self):
        file = open("VERSION", "r")
        return file.read().rstrip("\n")

    def get_random_talk(self):
        headers = {'user-agent': 'vtalks/updater-worker/' + self.get_version()}
        resp = requests.get(settings.VTALKS_API_RANDOM_TALK_URL, headers=headers)
        if resp.status_code != 200:
            return

        return resp.json()
