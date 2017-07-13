import logging
import os
from logging.handlers import RotatingFileHandler

from config.config import Config
from network.network import Network


def logger_setup(mode):
    if mode == 'dev':
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO

    log_formatter = logging.Formatter(Config.get('APP_LOG_FORMAT'), datefmt='%Y/%m/%d %H:%M:%S')
    loggers = ['ddd_network']

    handler = RotatingFileHandler('log.txt', maxBytes=10000000, backupCount=5)
    handler.setLevel(log_level)
    handler.setFormatter(log_formatter)

    for logger_name in loggers:
        logger = logging.getLogger(logger_name)
        logger.addHandler(handler)

    pass


def main():
    logger_setup(os.environ.get("SECRET_KEY"))
    Network()


if __name__ == '__main__':
    main()
