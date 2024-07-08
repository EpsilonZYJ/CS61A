from operator import add, mul

x = add(add(2, mul(3, 4)), 5)
y = (2 + 3) * (4 + 5)

div_ture = 2013 / 10
#true division: 201.3
div_inte = 2013 // 10
#interior division: 201

from operator import truediv, floordiv
print(truediv(2013, 10))
#201.3
print(floordiv(2013, 10))
#201

from operator import mod
print(mod(2013, 10))
#equals to 2013 % 10 : 3

def divide_exact(n, d):
    return n // d, n % d

quotient, remainder = divide_exact(2013, 10)
print(quotient, remainder)
#201 3
