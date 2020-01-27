#Debugging logging

import logging

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s-%(levelname)s-%(message)s')

'''
To save the logging in a file and not show on console:
    logging.basicConfig(filename = 'D://programLogs.txt',level = logging.DEBUG,
                                    format = '%(asctime)s-%(levelname)s-%(message)s')
'''
#logging.disable(logging.CRITICAL) #disable everything below CRITICAL,basically everything.
#logging.disable(logging.DEBUG)     #disable on DEBUG only.

#levels are DEBUG,INFO,WARNING,ERROR,CRITICAL.


logging.debug('Start of program')

def factorial(n):
    logging.info('Start of factorial (%s)' %n)
    total = 1
    for i in range (n+1):
        total *=i
        logging.critical('i is %s,total is %s.' %(i,total))
    logging.warning('return value is %s' %total)

    return total

print(factorial(5))

logging.debug('End of Program.')
