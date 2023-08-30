import logging
import pytz
from datetime import datetime

# Set the logging module's time zone to Singapoer Time (SGT)
logging.Formatter.converter = lambda *args: datetime.now(tz=pytz.timezone("Asia/Singapore")).timetuple()

def get_logger(name, log_level="DEBUG"):
    logger = logging.getLogger(name)

    # Validate the log level, any invalid log level will raise a ValueError
    log_level = log_level.upper()
    allowed_log_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    
    if log_level not in allowed_log_levels:
        raise ValueError(f"Invalid log level: {log_level}. Allowed log levels are: {allowed_log_levels}")
    
    # Set up the logger configuration and format
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s: %(asctime)s - %(module)s.%(funcName)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    
    logger.setLevel(logging.getLevelName(log_level))
    return logger
#end def
