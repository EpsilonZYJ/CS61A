def if_(c, t, f):
    if c:
        return t
    else:
        return f

from math import sqrt

def real_sqrt(x):
    """The real part of the square root of X"""
    if x > 0:
        return sqrt(x)
    else:
        return 0.0
    """
    return if_(x > 0, sqrt(x), 0.0)

    false: all the three expressions will be 
    evalute before calling
    """

""""""""""""""""""""""""""""""""""""""""""""""""""""""

from math import sqrt

def has_big_sqrt(x):
    return x > 0 and sqrt(x) > 10

def reasonable(n):
    return n == 0 or 1/n != 0

""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""Conditional Expression"""
x = 10
print(abs(1/x if x != 0 else 0))