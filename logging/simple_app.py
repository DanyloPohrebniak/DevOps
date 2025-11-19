import logging
logger = logging.getLogger(__name__)

def do_something():
    for i in range(0, 10):
        if i%2 == 0:
            logging.info(f"{i} is an even number")
        elif i%2 != 0:
            logging.warning(f"{i} is an odd number")
        elif i == 0:
            logging.error(f"{i} is a zero")
        else:
            logging.critical(f"{i} isn`t a number")