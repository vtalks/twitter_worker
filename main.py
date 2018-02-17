import os
import sys
import time
import logging

import schedule
import requests
import tweepy

from slugify import slugify


TWITTER_TWEET_LIMIT = 140


def get_random_talk():
    logging.debug("Get a random talk ...")
    r = requests.get('https://vtalks.net/api/random-talk/')
    if r.status_code != 200:
        logging.error("Can't fetch a random talk, response status code is", r.status_code)
        return
    return r.json()


def generate_tweet_content(talk_json):
    tweet_content = ""
    tweet_length = 0
    tweet_content += talk_json["title"]
    tweet_length += len(talk_json["title"])
    tweet_content += " "
    tweet_length += 1
    tweet_content += "https://vtalks.net/talk/{}".format(talk_json['slug'])
    # Twitter links always are 23 chars length (using t.co)
    # https://help.twitter.com/en/using-twitter/how-to-tweet-a-link
    tweet_length += 23

    # If there are remaining chars, add talk have tags, add them to the tweet,
    # starting from small to big by length.
    if talk_json["tags"]:
        tags = sorted(talk_json["tags"], key=len)
        for tag in tags:
            tag = slugify(tag, to_lower=True, separator="_")
            remaining_chars = TWITTER_TWEET_LIMIT - tweet_length
            if len(tag)+1 < remaining_chars:
                tweet_content += " "
                tweet_length += 1
                tweet_content += "#"+tag
                tweet_length += len(tag)+1
    return tweet_length, tweet_content


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
