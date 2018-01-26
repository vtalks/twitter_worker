import sys

import requests


def main(argv):
    # get a random talk
    r = requests.get('https://vtalks.net/api/random-talk')

    print(r.json())


if __name__ == "__main__":
    main(sys.argv[1:])
