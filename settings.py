import os

TWITTER_TWEET_LIMIT = 140

TLKSIO_TWITTER_TOKEN = os.environ.get('TLKSIO_TWITTER_TOKEN', "")
TLKSIO_TWITTER_SECRET = os.environ.get('TLKSIO_TWITTER_SECRET', "")
TLKSIO_TWITTER_ACCESS_TOKEN = os.environ.get('TLKSIO_TWITTER_ACCESS_TOKEN', "")
TLKSIO_TWITTER_ACCESS_SECRET = os.environ.get('TLKSIO_TWITTER_ACCESS_SECRET', "")

VTALKS_API_RANDOM_TALK_URL = 'https://vtalks.net/api/talk/random-talk/'