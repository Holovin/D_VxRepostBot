import asyncio
import signal

import sys

from dev.logger import logger_setup
from helpers.config import Config
from network.network_io import NetworkManager


def handler(loop):
    loop.remove_signal_handler(signal.SIGTERM)
    loop.stop()


async def task():
    async with NetworkManager() as network:
        await network.http_get('https://httpbin.org/ip')


def main():
    # TODO: wrap as coroutine?
    Config.load('config')

    logger_setup('log.txt', ['NetworkAsync'])

    loop = asyncio.get_event_loop()

    # TODO: windows?
    if sys.platform != 'win32':
        loop.add_signal_handler(signal.SIGTERM, handler)

    loop.run_until_complete(task())


async def test():
    print('1')
    pass


if __name__ == '__main__':
    main()