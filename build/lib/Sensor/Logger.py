import logging
import os
from datetime import datetime

# Define log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define log directory and create if it doesn't exist
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Full path to log file
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Configure logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format=" [ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s  - %(message)s ",
    level=logging.INFO,  # Fixed this line
)

# Create a logger object
logger = logging.getLogger(__name__)

# Test logging
if __name__ == "__main__":
    logger.info("Logging setup complete! Logger is working.")
