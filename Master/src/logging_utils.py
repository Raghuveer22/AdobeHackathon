import logging
import os

LOGFILEPATH = 'LogFile.log'

def setup_logging():
    """Set up logging configuration."""
    logging.basicConfig(
        level=os.environ.get("LOGLEVEL", "INFO"),
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(LOGFILEPATH)
        ]
    )
