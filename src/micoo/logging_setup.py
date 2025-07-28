"""Set up logging for the micoo application."""

import logging
import sys
from logging.handlers import RotatingFileHandler

from micoo.config import log_file_path

logger = logging.getLogger("micoo")
logger.setLevel(logging.INFO)

# Create a file handler that logs all messages
file_handler = RotatingFileHandler(
    log_file_path, maxBytes=10 * 1024 * 1024, backupCount=5
)
file_handler.setLevel(logging.INFO)

# Create a console handler for errors only
console_handler = logging.StreamHandler(sys.stderr)
console_handler.setLevel(logging.ERROR)

# Create a formatter and set it for both handlers
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
