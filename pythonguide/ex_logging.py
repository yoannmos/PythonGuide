"""
:module: ex_logging.py
"""

import logging

FORMAT = "[%(levelname)s] %(message)s"
logging.basicConfig(level=logging.DEBUG, format=FORMAT)


def factorial(n):
    """A factorial fonction

    :param n: The numper to factorize
    :type n: Integer

    :returns: Total  
    :rtype: Integer
    """
    logging.debug("Start of factorial {}".format(n))
    total = 1
    for i in range(n + 1):
        total *= i + 1
        logging.debug("i is " + str(i) + ", total is " + str(total))
    logging.debug("End of factorial {}".format(n))
    return total


if __name__ == "__main__":

    factorial(5)
