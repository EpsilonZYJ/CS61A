def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

from operator import add

m = curry2(add)
add_three = m(3)

print(add_three(2))
print(add_three(2010))

curry2 = lambda f: lambda x: lambda y: f(x, y)

m = curry2(add)
print(m(2)(3))