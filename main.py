import sys
import time
import logging

import schedule

from worker import get_random_talk
from worker import generate_tweet_content
from worker import post_tweet


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
    job()
    schedule.every(6).hours.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main(sys.argv[1:])
