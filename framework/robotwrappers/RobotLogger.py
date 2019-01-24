# coding=utf-8
import logging

# logger levels
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
INFO = 20
DEBUG = 10
NOTSET = 0


class RobotLogger(object):
    __logger = logging.getLogger("Robot Logger")

    @staticmethod
    def set_level(level=INFO):
        RobotLogger.__logger.setLevel(level)

    @staticmethod
    def info(message):
        RobotLogger.__logger.info(msg=message)

    @staticmethod
    def warning(message):
        RobotLogger.__logger.warning(msg=message)

    @staticmethod
    def debug(message):
        RobotLogger.__logger.debug(msg=message)

    @staticmethod
    def error(message):
        RobotLogger.__logger.error(msg=message)

    @staticmethod
    def fatal(message):
        RobotLogger.__logger.fatal(msg=message)
