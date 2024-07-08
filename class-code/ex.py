"""
    interactive session
    python3 -m doctest ex.py    no output
    python3 -m doctest -v ex.py     output
"""
from operator import floordiv, mod

def divide_exact(n, d):
    """Return the quotient and remainder of dividing N by D.

    >>>q, r = divide_exact(2013, 10)
    >>>q
    201
    >>>r
    3
    """
    return floordiv(n, d), mod(n, d)

def absolute_value(x):
    """Return the absolute value of x."""
    if x < 0:           #header
        return -x       #statement      #suite
    elif x == 0:
        return 0
    else:
        return x
    
#false values in python: false, 0, '', None


"""while statement"""
i, total = 0, 0
while i < 3:
    i = i + 1
    total = total  + i
