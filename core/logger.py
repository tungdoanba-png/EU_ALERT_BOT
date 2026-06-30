"""
=========================================================
LOGGER
=========================================================
"""

import logging
import os

from config import LOG_FILE, LOG_LEVEL


# Tạo thư mục logs nếu chưa có
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)


logger = logging.getLogger("EU_ALERT_BOT")

logger.setLevel(getattr(logging, LOG_LEVEL.upper()))


formatter = logging.Formatter(
    "[%(asctime)s] %(levelname)s | %(message)s",
    "%Y-%m-%d %H:%M:%S"
)


# Ghi file
file_handler = logging.FileHandler(
    LOG_FILE,
    encoding="utf-8"
)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


# Hiển thị Terminal
console_handler = logging.StreamHandler()

console_handler.setFormatter(formatter)

logger.addHandler(console_handler)


logger.propagate = False