import logging
import pytz
from datetime import datetime

# Set the logging module's time zone to Singapoer Time (SGT)
logging.Formatter.converter = lambda *args: datetime.now(tz=pytz.timezone("Asia/Singapore")).timetuple()

# Set up the logger configuration and format
logging.basicConfig(
    level=logging.DEBUG, 
    format="%(asctime)s - %(name)s - %(levelname)-8s - %(module)s.%(funcName)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger("custom_logger")

# Test log message
# logger.info("This is an example log message.")