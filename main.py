import os
import sys
import time
import logging

import schedule
import requests
import tweepy


def get_random_talk():
    logging.debug("Get a random talk ...")
    r = requests.get('https://vtalks.net/api/random-talk/')
    if r.status_code != 200:
        logging.error("Can't fetch a random talk, response status code is", r.status_code)
        return
    return r.json()


def generate_tweet_content(talk_json):
    content = ""
    content += talk_json["title"]
    content += " "
    content += "https://vtalks.net/talk/{}".format(talk_json['slug'])
    return content


def post_tweet(tweet_content):
    TLKSIO_TWITTER_TOKEN = os.environ['TLKSIO_TWITTER_TOKEN']
    TLKSIO_TWITTER_SECRET = os.environ['TLKSIO_TWITTER_SECRET']
    TLKSIO_TWITTER_ACCESS_TOKEN = os.environ['TLKSIO_TWITTER_ACCESS_TOKEN']
    TLKSIO_TWITTER_ACCESS_SECRET = os.environ['TLKSIO_TWITTER_ACCESS_SECRET']
    twitter_auth = tweepy.OAuthHandler(TLKSIO_TWITTER_TOKEN, TLKSIO_TWITTER_SECRET)
    twitter_auth.set_access_token(TLKSIO_TWITTER_ACCESS_TOKEN, TLKSIO_TWITTER_ACCESS_SECRET)
    twitter = tweepy.API(twitter_auth)
    return twitter.update_status(tweet_content)


def job():
    talk_json = get_random_talk()
    if not talk_json:
        return
    logging.debug(talk_json)
    tweet_content = generate_tweet_content(talk_json)
    status = post_tweet(tweet_content)
    logging.debug("TWEET:", status)


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
