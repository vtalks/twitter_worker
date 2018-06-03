import sys
import logging

from worker import worker


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    args = sys.argv[1:]

    twitter_worker = worker.Worker()

    twitter_worker.job()

    twitter_worker.run(args)
