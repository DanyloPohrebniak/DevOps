"""Simple app to test logging"""
import logging

logger = logging.getLogger(__name__)

def do_something():
    """Demonstrate logging with different levels"""
    for i in range(0, 10):
        if i == 0:
            logging.error("%s is a zero", i)
        elif i%2 == 0:
            logging.info("%s is an even number", i)
        elif i%2 != 0:
            logging.warning("%s is an odd number", i)
        else:
            logging.critical("%s isn`t a number", i)
            