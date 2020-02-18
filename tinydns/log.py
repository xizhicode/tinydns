# coding:utf-8
# write by zhou
import logging
from logging import handlers, Formatter


def get_logger(log_name, backupCount=7, *args, **kwargs):
    """
    init logger
    :param log_name:
    :param backupCount:
    :param args:
    :param kwargs:
    :return:
    """
    logger = logging.getLogger()
    handler = handlers.TimedRotatingFileHandler(log_name, when='D', backupCount=backupCount)
    formatter = Formatter('[%(asctime)s: %(levelname)s]: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger


if __name__ == '__main__':
    logger = get_logger('test.log')
    logger.info('TEST')