import logging
import aiohttp
import asyncio
import async_timeout


class NetworkManager:
    logger_name = 'NetworkAsync'
    logger = logging.getLogger(logger_name)
    logger.addHandler(logging.NullHandler())

    def __init__(self, headers=None):
        if not headers:
            self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:2.0b7) Gecko/20100101 Firefox/4.0b7'}
        else:
            self.headers = headers

    async def __aenter__(self):
        self.session = aiohttp.ClientSession(headers=self.headers)
        return Network(self.session, NetworkManager.logger)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # TODO: handle exceptions?
        self.session.close()


class Network:
    def __init__(self, session, logger):
        self.logger = logger
        self.last_answer = None
        self.session = session

    async def http_get(self, url, url_params=None):
        try:
            response = await aiohttp.request('GETT', url, params=url_params)

            self.last_answer = await response.json()

            print(self.last_answer)

        except Exception as e:
            self.logger.warn('[Expection] {}'.format(e))
            return False

        self.logger.debug('test')

        return self.last_answer
