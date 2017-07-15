from subprocess import Popen, TimeoutExpired

import sys
from time import sleep

from config.config import Config
from dev.logger import logger_setup
from network.network import Network
from storage import userModel, subModel
from storage.storage import Storage


def main():
    # logger_setup(Config.get('APP_LOG_FILE'), [Network.logger_name])
    # Network()
    # db = Storage.get()
    # db.connect()
    # db.disconnect()

    telegram_bot = Popen(Config.get('APP_TELEGRAM_BOT_FILE'), shell=True)
    vk_feed_parser = Popen(Config.get('APP_VK_FEED_PARSER_FILE'), shell=True)

    try:
        while True:
            if check_process(telegram_bot) is True:
                print('telegram ok')

            if check_process(vk_feed_parser) is True:
                print('vk feed ok')

            sleep(1)

    except KeyboardInterrupt:
        print('App stop...')
        sys.exit()


def check_process(process):
    try:
        process.wait(1)
        return False

    except TimeoutExpired:
        return True

    except Exception as e:
        print(e)
        return False

if __name__ == '__main__':
    main()
