import time
import logging

import schedule

from api import get_random_talk
from twitter import generate_tweet_content
from twitter import post_tweet


def job():
    talk_json = get_random_talk()
    if not talk_json:
        return
    tweet_length,  tweet_content = generate_tweet_content(talk_json)
    status = post_tweet(tweet_content)
    logging.debug(status)


def main(argv):
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Starting twitter-worker ...')

    schedule.every(6).hours.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
