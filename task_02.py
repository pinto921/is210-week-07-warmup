#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" if statement practice yes or no value"""

def bool_to_str(bval)
    """ a function to return yes or no to the truthiness of the argument

    Args:
        bval (mixed) : a boolean or boolean-like value to be tested

    Returns:
        str: yes for truth value, no for falsy value

    examples:
        >>> bool_to_str(1)
        'yes'

        >>> bool_to_str('')
        'No'
    """
    if bval:
        string = 'yes'
    else:
        string = 'no'
    return string
