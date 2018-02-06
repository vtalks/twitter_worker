import os
import sys
import time
import logging

import schedule
import requests
import tweepy


def tweet_content(talk_json):
    content = ""
    content += talk_json["title"]
    content += " "
    content += "https://vtalks.net/talk/{}".format(talk_json['slug'])
    return content


def job():
    logging.info("Get a random talk ...")
    # get a random talk
    r = requests.get('https://vtalks.net/api/random-talk/')
    if r.status_code != 200:
        logging.debug("Can't fetch a random talk, response status code is",
              r.status_code)
        exit(1)

    talk_json = r.json()

    TLKSIO_TWITTER_TOKEN = os.environ['TLKSIO_TWITTER_TOKEN']
    TLKSIO_TWITTER_SECRET = os.environ['TLKSIO_TWITTER_SECRET']
    TLKSIO_TWITTER_ACCESS_TOKEN = os.environ['TLKSIO_TWITTER_ACCESS_TOKEN']
    TLKSIO_TWITTER_ACCESS_SECRET = os.environ['TLKSIO_TWITTER_ACCESS_SECRET']

    auth = tweepy.OAuthHandler(TLKSIO_TWITTER_TOKEN, TLKSIO_TWITTER_SECRET)
    auth.set_access_token(TLKSIO_TWITTER_ACCESS_TOKEN, TLKSIO_TWITTER_ACCESS_SECRET)

    twitter = tweepy.API(auth)

    content = tweet_content(talk_json)

    status = twitter.update_status(content)

    print("TWEET:", status)


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
