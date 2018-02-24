import unittest

import settings


class TwitterWorkerSettingsTest(unittest.TestCase):

    def test_default_settings(self):
        self.assertEqual(settings.TWITTER_TWEET_LIMIT, 140)
