# logger.py
# App logger
# r2

import logging
from logging.handlers import RotatingFileHandler


class DDLogger:
    logger_name = 'ddlogger'
    logger = logging.getLogger(logger_name)

    @staticmethod
    def __init__(log_file, loggers_list=None, touch_root=True, log_level=logging.INFO, write_to_console=False,
                 formatter='%(module)-16s %(levelname)-8s [%(asctime)s] %(message)s', datefmt='%Y/%m/%d %H:%M:%S',
                 backup_count=1, logger_propagate=False, global_logger_name='ddlogger'):
        DDLogger.logger_name = global_logger_name
        DDLogger.logger = logging.getLogger(global_logger_name)

        log_formatter = logging.Formatter(formatter, datefmt=datefmt)

        root = logging.getLogger()

        if touch_root:
            root.setLevel(log_level)
            root.addHandler(logging.NullHandler())

            if write_to_console:
                console = logging.StreamHandler()
                console.setLevel(log_level)
                console.setFormatter(log_formatter)

                root.addHandler(console)
                root.info('Console output enabled')
        else:
            if write_to_console:
                print('[WARN] Cant write to console without touch_root=True')

        handler = RotatingFileHandler(log_file, backupCount=backup_count, encoding='utf8')
        handler.setLevel(log_level)
        handler.setFormatter(log_formatter)
        handler.doRollover()

        if loggers_list:
            for logger_name in loggers_list:
                logger = logging.getLogger(logger_name)
                logger.setLevel(log_level)
                logger.addHandler(handler)
                logger.propagate = logger_propagate

                if touch_root and console and write_to_console:
                    logger.addHandler(console)
        else:
            print('[WARN] Cant write to console without touch_root=True')

    @staticmethod
    def critical(message):
        DDLogger.__write(logging.CRITICAL, message)

    @staticmethod
    def fatal(message):
        DDLogger.__write(logging.FATAL, message)

    @staticmethod
    def error(message):
        DDLogger.__write(logging.ERROR, message)

    @staticmethod
    def warning(message):
        DDLogger.__write(logging.WARNING, message)

    @staticmethod
    def info(message):
        DDLogger.__write(logging.INFO, message)

    @staticmethod
    def debug(message):
        DDLogger.__write(logging.DEBUG, message)

    @staticmethod
    def __write(level, message):
        DDLogger.logger.log(level, '{}'.format(message))
