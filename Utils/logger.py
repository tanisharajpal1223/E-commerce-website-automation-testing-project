import logging
import os
from datetime import datetime

def get_logger():

    logger = logging.getLogger("test_logger")

    # ❗ Prevent duplicate handlers
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    # Create logs folder
    if not os.path.exists("logs"):
        os.makedirs("logs")

    log_file = f"logs/test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Format
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger