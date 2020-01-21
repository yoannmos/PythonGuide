import logging

# FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
FORMAT = '[%(levelname)s] %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
logging.debug('Start program')


def factorial(n):
    logging.debug('Start of factorial {}'.format(n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial {}'.format(n))
    return total


factorial(5)
logging.debug('End of program')
