import sys

import schedule
import requests


def tweet_content(talk_json):
    content = ""
    content += talk_json["title"]
    content += " "
    content += "https://vtalks.net/talk/{}".format(talk_json['slug'])
    return content


def job():
    # get a random talk
    r = requests.get('https://vtalks.net/api/random-talk')
    if r.status_code != 200:
        print("Can't fetch a random talk, response status code is",
              r.status_code)
        exit(1)

    talk_json = r.json()

    content = tweet_content(talk_json)

    print("TWEET:", content)


def main(argv):
    print('Get a random talk ...')

    schedule.every().hours(6).do(job)

    print("Tweeted.")


if __name__ == "__main__":
    main(sys.argv[1:])
