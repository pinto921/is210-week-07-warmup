#!/usr/bin/env python
# -*- coding: utf- -*-

""" a function to return a maximum value, minimum value and an average"""

import decimal

def lexicographics(to_analyze):
    """ it calculates the max. min. and the average lenght of words in a speech

    Args:
        to_analyze (str): a string to be analyzed

    Returns:
    Tuple: the max line in to_analyze, the men line, and the average line

    Example:
        >>> lexicographics('''dont stop believing,
        hold on to that feeling.''')
        (5, 3, decimal('4'))

        >>>lexicographics('''dont stop believing,
        hold on to that feeling.
        forever and ever.''')
        (5,3, decimal('3.6666666666666666666666666667'))
    """

    line = to_analyze.split('\n')
    word_count = []
    for words in line:
        len_line = len(words.spit())
        word_count.append(len_line)
    ave = decimal.Decimal(sum(word_count))/len(word_count)
    return max(word_count), min(word_count), ave
