"""
String representation
"""
from fractions import Fraction
half = Fraction(1, 2)
half # Fraction(1, 2)
repr(half) # 'Fraction(1,2)'
str(half) # '1/2'
print(half) # 1/2
eval(repr(half)) # Fraction(1, 2)
eval(str(half)) # 0.5
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
Polymorphic Fuctions
"""
half.__repr__()  # 'Fraction(1, 2)'
half.__str__() # '1/2'

class Bear:
    """A Bear."""
    def __init__(self):
        self.__repr__ = lambda: 'oski'
        self.__str__ = lambda: 'this bear' 
    
    def __repr__(self):
        return 'Bear()'
   
    def __str__(self):
        return 'a bear'
    
oski = Bear()
print(oski)
print(str(oski))
print(repr(oski))
print(oski.__str__())
print(oski.__repr__())

def repr(x):
    return type(x).__repr__(x)

def str(x):
    t = type(x)
    if hasattr(t, '__str__'):
        return t.__str__(x)
    else:
        return repr(x)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
interfaces
"""    
class Ratio:
    def __init__(self, n, d):
        self.numer = n
        self.denom = d

    def __repr__(self):
        return 'Ratio{0}, {1}'.format(self.numer, self.denom)
    
    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)
    
    def __add__(self, other):
        if isinstance(other, int):
            n = self.numer + self.denom * other
            d = self.denom
        elif isinstance(other, Ratio):
            n = self.numer * other.denom + self.denom * other.numer
            d = self.denom * other.denom
        elif isinstance(other, float):
            return float(self) + other
        g = gcd(n, d)
        return Ratio(n//g, d//g)
    __radd__ = __add__
    
    def __float__(self):
        return self.numer/self.denom
    
def gcd(n, d):
    while n !=d :
        n, d = min(n, d), abs(n-d)
    return n
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
Special method
"""    
zero, one, two = 1, 2, 3
one.__add__(two) # 3
zero.__bool__(), one.__bool__() # (False, True)






















































