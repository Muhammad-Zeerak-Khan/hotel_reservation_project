import logging
import os
from datetime import datetime

LOGS_DIR: str = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)
LOG_FILE: str = os.path.join(
    LOGS_DIR, f"log_{datetime.now().strftime('%d_%m_%Y-%H_%M_%S')}"
)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s",
)


def get_logger(name) -> logging.Logger:
    logger: logging.Logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger
