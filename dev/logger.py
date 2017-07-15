import logging
from logging.handlers import RotatingFileHandler
from config.config import Config


def logger_setup(log_file, loggers=None):
    mode = Config.get('APP_WORK_MODE')

    if mode == 'dev':
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO

    log_formatter = logging.Formatter(Config.get('APP_LOG_FORMAT'), datefmt='%Y/%m/%d %H:%M:%S')

    handler = RotatingFileHandler(log_file, maxBytes=10000000, backupCount=5)
    handler.setLevel(log_level)
    handler.setFormatter(log_formatter)

    if loggers is None:
        loggers = []

    for logger_name in loggers:
        logger = logging.getLogger(logger_name)
        logger.addHandler(handler)
