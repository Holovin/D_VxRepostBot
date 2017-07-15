import random
from time import sleep

import sys


def main():
    r = random.Random()

    try:
        while True:
            sleep(r.randint(5, 5))
            print('2. bot')

    except KeyboardInterrupt:
        print('App bot stop...')
        sys.exit()


if __name__ == '__main__':
    main()