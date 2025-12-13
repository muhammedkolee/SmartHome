import logging
from logging.handlers import RotatingFileHandler
from queue import Queue

log_queue = Queue()

def setup_logger():
    logger = logging.getLogger("SmartHome")
    logger.setLevel(logging.INFO)

    file_handler = RotatingFileHandler(
        "smarthome.log",
        maxBytes=1_000_000,  # 1 MB
        backupCount=5
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(threadName)s | %(message)s"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
