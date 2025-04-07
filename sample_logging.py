i#Python script to redirect the logs on to the console and print on the console

import logging

logging.basicConfig(level= logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


#creating logger object to either create or retrieve the logger
logger=logging.getLogger('logging_sample3')

#setting the global log level --> logger will handle the messages from this level
logger.setLevel(logging.DEBUG)

#creating the handler using StreamHandler function to direct the logs to console
console_handler = logging.StreamHandler()
#setting the global log level --> handler will handle the messages from this level
console_handler.setLevel(logging.DEBUG)

#creating a formatter using Formatter function to set the structure of the log messages
console_handler.setFormatter(formatter)

#adding an additional logging handler using addHandler function to print logs on the console
logger.addHandler(console_handler)

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
