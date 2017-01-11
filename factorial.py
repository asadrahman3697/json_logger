#! python

from logger import Logger

logger = Logger(logfile=True)

logger.info('Start of Program')

def factorial(n):
    logger.debug('Start of factorial(%s)' %(n))
    
    total = 1
    for i in range(1, n + 1):
        total *=i
        logger.debug('i is ' + str(i) + ' , total is ' + str(total))
        
    logger.debug('End of factorial(%s)' %(n))
    return total
    
print(factorial(5))

logger.info('End of program')

