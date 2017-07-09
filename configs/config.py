import logging


class Config:
    LOG_FORMAT = '%(module)-8s %(levelname)-8s [%(asctime)s] %(message)s'
    LOG_LEVEL = logging.DEBUG
    TIMEZONE = 'Europe/Minsk'

    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:2.0b7) Gecko/20100101 Firefox/4.0b7'}