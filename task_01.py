#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Fibonacci sequence generator fucntion with our while loop"""

def fibonacci(maxint)
    """ fibonacci with a maximum value

    Args:
        maxint (int): an integer that serves as the upper bound of the loop

    Returns:
        list: a series of fibonacci numbers

    Examples:
        >>> fibonacci(10)
        [0,1,2,3,5,8,13]

        >>> fibonacci(20
        [0,1,1,2,3,5,8,13]
    """
    a, b = 0,1
    series = [a]
    while b <= maxint:
        series.append(b)
        a,b = b, a+b

    return series 
