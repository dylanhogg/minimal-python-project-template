import os
import sys
from loguru import logger


def configure(remove_existing=True, logfile="./log/app.log"):
    if remove_existing:
        logger.remove()
    logger.add(sys.stderr, level=os.getenv("LOG_STDERR_LEVEL", "INFO"))
    logger.add(
        logfile,
        level=os.getenv("LOG_FILE_LEVEL", "DEBUG"),
        rotation=os.getenv("LOG_FILE_ROTATION", "00:00"),
    )
