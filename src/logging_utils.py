import logging
import os
BASEPATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOGFILEPATH = os.path.join(BASEPATH,'output','LogFile.log')  # Specify the path to the log file

def setup_logging():
    """Set up logging configuration."""
    logging.basicConfig(
        level=os.environ.get("LOGLEVEL", "INFO"),  # Set the log level to the value of the LOGLEVEL environment variable or INFO if not set
        format='%(asctime)s - %(levelname)s - %(message)s',  # Specify the log message format
        handlers=[
            logging.StreamHandler(),  # Add a stream handler to log messages to the console
            logging.FileHandler(LOGFILEPATH)  # Add a file handler to log messages to the specified log file
        ]
    )
