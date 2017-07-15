import random
from time import sleep

import sys


def main():
    r = random.Random()

    try:
        while True:
            sleep(r.randint(5, 5))
            print('1. feed')

    except KeyboardInterrupt:
        print('App feed stop...')
        sys.exit()


if __name__ == '__main__':
    main()