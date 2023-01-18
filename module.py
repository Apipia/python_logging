# Every file should have these two lines at the top somewhere:
import logging
logger = logging.getLogger(__name__)


def module_function():
    logger.info("Logging from module.module_function")
    pass
