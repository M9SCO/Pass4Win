import logging
import os
import sys

from data.logger import GlobalFilter


def make_logger():
    FORMAT = "%(asctime)s <%(name)s %(threadName)s> [%(levelname)s] -- %(message)s"
    console = logging.StreamHandler(sys.stdout)
    console_lvl = logging.INFO
    console.setLevel(console_lvl)
    console.addFilter(GlobalFilter(logging.INFO))

    file_log = logging.FileHandler(f"resources{os.sep}.log")
    file_log.setLevel(logging.INFO)
    error = logging.StreamHandler()
    error.setLevel(logging.WARNING)

    logging.basicConfig(format=FORMAT, level=logging.INFO, handlers=[console, error, file_log])
