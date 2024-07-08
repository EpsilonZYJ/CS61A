"""
iterators
"""
s = [3, 4, 5]
t = iter(s)
next(t)

d = {'one': 1, 'two': 2, 'three': 3}
d['zero'] = 0
k = iter(d.keys()) # or iter(d)
next(k) # one
next(k) # two
next(k) # three 
next(k) # zero

v = iter(d.values())
next(v) # 1
next(v) # 2 
next(v) # 3 
next(v) # 0

i = iter(d.items())
next(i) # ('one', 1)
next(i) # ('two', 2)
next(i) # ('three', 3)
next(i) # ('zero', 0)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
For statement
"""

r = range(3, 6)
list(r)

for i in r:
    print(i) # 3 4 5

ri = iter(r)
next(ri)
for i in ri:
    print(i) # 4 5

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
Built-in functions for iteration
"""

bcd = ['b', 'c', 'd']
[x.upper() for x in bcd]
m = map(lambda x: x.upper(), bcd)
next(m) # 'B'
next(m) # 'C'
next(m) # 'D'

def double(x):
    print('**', x, '=>', 2*x, '**')
    return 2*x

m = map(double, [3, 5, 7])
next(m) # ** 3 => 6 ** 6
next(m) # ** 5 => 10 ** 10 
next(m) # ** 7 => 14 ** 14 

m = map(double, [3, 5, 7])
f = lambda y: y >= 10
t = filter(f, m)
next(t)
'''
** 3 => 6 ** 
** 4 => 8 **
** 5 => 10 **
10
'''

next(t)
'''
** 6 => 12 **
12
'''

t = [1, 2, 3, 2, 1]
reversed(t) == t # False
list(reversed(t)) == t #True


d = {'a': 1, 'b': 2}
items = iter(d.items())
next(items) # ('b', 2)
next(items) # ('a', 1)

items = zip(d.keys(), d.values())
next(items) # ('b', 2)
next(items) # ('a', 1)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
Generators
"""

def plus_minus(x):
    yield x
    yield -x
t = plus_minus(3)
next(t) # 3
next(t) # -3

def even(start, end):
    even = start + (start%2)
    while even < end:
        yield even
        even += 2

def a_then_b_1(a, b):
    for x in a:
        yield x
    for x in b:
        yield x

def a_then_b_2(a, b):
    yield from a
    yield from b

list(a_then_b_1([3, 4], [5, 6]))    # [3, 4, 5, 6]
def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k-1)
    else:
        yield 'Blast off'

def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s
        
def substring(s):
    if s:
        yield from prefixes(s)
        yield from prefixes(s[1:])



