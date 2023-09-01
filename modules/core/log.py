import logging
import sys

logger = logging.getLogger()

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

# logger.setLevel(logging.INFO)
logger.addHandler(console_handler)
