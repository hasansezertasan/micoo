"""Set up logging for the micoo application."""

import logging

from micoo.config import log_file_path

logger = logging.getLogger("micoo")
logger.setLevel(logging.ERROR)
# Create a file handler that logs error messages
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.ERROR)
# Create a formatter and set it for the handler
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
# Add the handler to the logger
logger.addHandler(file_handler)
