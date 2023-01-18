import logging
import os
import requests
from logging.handlers import RotatingFileHandler
from module import module_function

logger = logging.getLogger(__name__)


def setup_logging(log_level="INFO"):
    # Root logger is configured with formatter and handler
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    formatter = logging.Formatter(
        "[%(levelname)s] time:$(asctime)s thread:%(threadName)s func:%(funcName)s msg:%(message)s",
    )
    handler = RotatingFileHandler("app_logs.log", mode="a", maxBytes=1024*1024*2)
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)
    root_logger.info("Logging Setup Complete: {}".format(log_level))


def example_function():
    # Example of logging from a function
    logger.info("Logging from example_function")


def main():
    # First thing first, setup_logging
    setup_logging(os.environ.get("LOG_LEVEL", "INFO"))
    logger.info("Application Starting")
    module_function()
    logger.info("If log-level set to DEBUG, you should see some logs from requests module next.")
    # only DEBUG log-level requests will be logged by modules (typically).
    requests.get("https://www.google.com")
    logger.info("Application completed successfully")


if __name__ == '__main__':
    main()

