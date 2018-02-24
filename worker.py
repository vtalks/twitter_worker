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

    logging.debug("Talk id:{} title:{} url:{} tags:{}".format(
        talk_json['id'],
        talk_json['title'],
        talk_json['youtube_url'],
        ",".join(talk_json['tags']),
    ))

    tweet_length,  tweet_content = generate_tweet_content(talk_json)

    logging.debug("Create {} chars tweet: {}".format(
        tweet_length,
        tweet_content
    ))

    status = post_tweet(tweet_content)

    logging.debug("Tweet published successfully id:{}".format(
        status.id_str
    ))


def main(argv):
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Starting twitter-worker ...')

    schedule.every(6).hours.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
