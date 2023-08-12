import os
import logging
import pytz
from datetime import datetime

# Set the logging module's time zone to Singapoer Time (SGT)
logging.Formatter.converter = lambda *args: datetime.now(tz=pytz.timezone("Asia/Singapore")).timetuple()

def setup_custom_logger(name):
    logger = logging.getLogger(name)

    # Set up the logger configuration and format
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)-8s - %(module)s.%(funcName)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Set the logger level based on the environment variable
    log_level = os.environ.get("LOG_LEVEL", "DEBUG")  # Use 'DEBUG' as default
    logger.setLevel(logging.getLevelName(log_level.upper()))


    return logger