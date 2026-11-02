
import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logger():
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("cloud_devops")
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    file_handler = RotatingFileHandler(
        "logs/application.log",
        maxBytes=1024 * 1024,
        backupCount=3
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

