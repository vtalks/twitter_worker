import unittest

from tests.tests_data import fake_talk_json

from worker.twitter import Twitter


class TwitterTest(unittest.TestCase):

    def test_generate_tweet_content(self):
        twitter = Twitter()
        tweet_length, tweet_content = twitter.generate_tweet_content(fake_talk_json)

        self.assertGreater(tweet_length, 0)

        self.assertIsNotNone(tweet_content)
        self.assertIn("https://vtalks.net/talk/josh-mcclain-black-magic-apis-jsconf2014", tweet_content)
