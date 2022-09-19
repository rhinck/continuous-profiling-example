from custom_logging.logger import custom_logger

import time


def simple_func():
    time.sleep(3)
    custom_logger.info("hello world", extra={"id": 1})
    second_func()

def second_func():
    custom_logger.info("second func")