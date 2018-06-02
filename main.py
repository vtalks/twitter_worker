import sys
import logging

from worker import worker


if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    logging.info('Starting twitter-worker ...')

    args = sys.argv[1:]

    twitter_worker = worker.Worker()

    logging.info("Executing once as a task")
    twitter_worker.job()

    logging.info("Executing the job scheduler")
    twitter_worker.run(args)
