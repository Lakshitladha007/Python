import logging

logging.basicConfig(
    filename='app.log',           # File name
    level=logging.DEBUG,          # Minimum log level to capture
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
)

logging.debug("This is a DEBUG message")
logging.info("This is an INFO message")
logging.warning("This is a WARNING")
logging.error("This is an ERROR")
logging.critical("This is CRITICAL")
