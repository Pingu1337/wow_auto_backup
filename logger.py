import logging
import os

def createLogger():

    if not os.path.isdir('logs'):
        os.mkdir('logs')
        os.mkdir('logs/debug')

    debuglogs = 'logs/debug/debug.log'
    logs = 'logs/logs.log'

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler(debuglogs)
    fh.setLevel(logging.DEBUG)

    # create console handler with a higher log level
    ch = logging.FileHandler(logs)
    ch.setLevel(logging.WARNING)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # add the handlers to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger