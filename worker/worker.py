import time
import logging

import schedule

from worker.api import API
from worker.twitter import Twitter


class Worker:

    def job(self):
        api = API()

        talk_json = api.get_random_talk()
        if not talk_json:
            return

        logging.debug("Talk id:{} title:{} url:{} tags:{}".format(
            talk_json['id'],
            talk_json['title'],
            talk_json['youtube_url'],
            ",".join(talk_json['tags']),
        ))

        twitter = Twitter()

        tweet_length,  tweet_content = twitter.generate_tweet_content(talk_json)

        logging.debug("Tweet {} chars: {}".format(
            tweet_length,
            tweet_content
        ))

        status = twitter.post_tweet(tweet_content)

        logging.debug("Tweet published successfully id:{}".format(
            status.id_str
        ))

    def run(self, argv):
        schedule.every(6).hours.do(self.job)
        while True:
            schedule.run_pending()
            time.sleep(1)
