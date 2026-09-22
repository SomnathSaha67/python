import logging

logging.basicConfig(level= logging.INFO)

logging.debug("This is a DEBUG message")
logging.info("This is an INFO message")
logging.warning("This is a WARNING message")
logging.error("This is an ERROR message")
logging.critical("This is a CRITICAL message")

# At INFO level, the DEBUG message does not appear in the output.
# Only INFO, WARNING, ERROR, and CRITICAL are shown.

# DEBUG level
logging.basicConfig(level= logging.DEBUG, force= True)

logging.debug("This is a DEBUG message")
logging.info("This is an INFO message")
logging.warning("This is a WARNING message")
logging.error("This is an ERROR message")
logging.critical("This is a CRITICAL message")

# At DEBUG level, all five messages appear, including DEBUG.