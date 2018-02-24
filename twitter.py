import tweepy
from slugify import slugify

import settings


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
            remaining_chars = settings.TWITTER_TWEET_LIMIT - tweet_length
            if len(tag)+1 < remaining_chars:
                tweet_content += " "
                tweet_length += 1
                tweet_content += "#"+tag
                tweet_length += len(tag)+1
    return tweet_length, tweet_content


def post_tweet(tweet_content):
    twitter_auth = tweepy.OAuthHandler(settings.TLKSIO_TWITTER_TOKEN, settings.TLKSIO_TWITTER_SECRET)
    twitter_auth.set_access_token(settings.TLKSIO_TWITTER_ACCESS_TOKEN, settings.TLKSIO_TWITTER_ACCESS_SECRET)
    twitter = tweepy.API(twitter_auth)
    return twitter.update_status(tweet_content)