import logging
from logging.handlers import RotatingFileHandler

from configs.config import Config
from helpers.network import Network


def logger_setup():
    log_formatter = logging.Formatter(Config.LOG_FORMAT, datefmt='%Y/%m/%d %H:%M:%S')
    loggers = ['ddd_network']

    handler = RotatingFileHandler('log.txt', maxBytes=10000000, backupCount=5)
    handler.setLevel(Config.LOG_LEVEL)
    handler.setFormatter(log_formatter)

    for logger_name in loggers:
        logger = logging.getLogger(logger_name)
        logger.addHandler(handler)

    pass

if __name__ == '__main__':
    logger_setup()

    a = Network()
