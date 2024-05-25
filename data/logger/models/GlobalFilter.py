import logging


class GlobalFilter(logging.Filter):
    def __init__(self, level, name=""):
        self.__level = level
        super(GlobalFilter, self).__init__(name)

    def filter(self, log_record):
        return log_record.levelno <= self.__level
