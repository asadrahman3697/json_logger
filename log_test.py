#! python
from logger import Logger

logger = Logger(logfile=True)

def main():

    logger.info('This is a info message')
    logger.debug('This is a debug message')
    logger.warning('This is a warning message')
    logger.error('This is a warning message')
    logger.critical('This is a warning message')
    
    
if __name__ == '__main__':
    main()
