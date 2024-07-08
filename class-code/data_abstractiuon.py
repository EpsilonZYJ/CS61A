"""
Data abstraction
"""
def mul_rational(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def add_rational(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def equal_rationals(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
Pairs
"""
pair = [1, 2]
x, y = pair

from operator import getitem
x = getitem(pair, 0)  # 1

from fractions import gcd

def rational(n, d):
    """Construct a rational number x that represents n/d."""
    g = gcd(n, d)
    return [n//g, d//g]



""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
Abstraction barriers
"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
constructors and selectors
"""
def print_rational(x):
    print(numer(x), '/', denom(x))

def rational(n, d):
    """Construct a rational number x that represents n/d."""
    def select(name):
        if name == 'n':
            return n
        elif name == 'd':
            return d
    return select

def numer(x):
    """Return the numerator of rational number x."""
    return x('n')

def denom(x):
    """Return the denominator of rational number x."""
    return x('d')

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
Dictionary
"""

numerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

numerals['I']  # 1
numerals.keys()  # dict_keys(['I', 'V', 'X', 'L', 'C', 'D', 'M'])
numerals.values()  # dict_values([1, 5, 10, 50, 100, 500, 1000])
numerals.items()  # dict_items([('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])

items = [('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)]
dict(items)  # {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
dict(items)['I']  # 1\

'X' in numerals  # True
numerals.get('A', 0)  # 0

squares = {x: x*x for x in range(10)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
squares[7]  # 49

{1:2, 1:3}  # {1: 3}
{1:[1, 2]}
