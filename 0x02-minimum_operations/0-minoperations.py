#!/usr/bin/python3
""" 0-minoperations module"""


def minOperations(n):
    """
    Funcion returns fewest # of operations
    needed to result in exactly n H characters
    """
    # all outputs should be at least 2 char: (min, Copy All => Paste)
    if n < 2:
        return 0
    operations = 0
    root = 2
    while root <= n:
        # if n evenly divides by root
        if n % root == 0:
            # make total even-divisions by root = total operations
            operations += root
            # then set n as the remainder of the division
            n = n/root
            # then reduce root by one
            # to find remaining smaller values that evenly-divide n
            root -= 1
        # increment root until it evenly-divides n
        root += 1
    return operations
