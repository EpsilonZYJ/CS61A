"""
Objects
"""
from datetime import date
today = date(2024, 7, 4)
print(today)    # 2024-07-04
freedom = date(2024, 9, 2)
print(str(freedom - today)) # 60 days, 0:00:00
print(today.year)   # 2024
print(today.month)  # 7
print(today.day)    # 4

print(today.strftime("%A, %B %d")) # 'Thursday July 04'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
Strings
"""

s = 'Hello'
print(s.upper())    # 'HELLO'
print(s.lower())    # 'hello'
print(s.swapcase()) # 'hELLO'
print(s)            # 'Hello'

a = 'A'
print(ord(a))   # 65
print(hex(ord(a)))  # 0x41
print(chr(65))  # 'A'

from unicodedata import name, lookup
print(name('A'))    # 'LATIN CAPITAL LETTER A'
print(name('a'))    # 'LATIN SMALL LETTER A'
print(lookup('WHITE SMILING FACE'))    # '☺'
print(lookup('SNOWMAN'))    # '☃'
print(lookup('BABY'))    # '👶'
print(lookup('SOCCER BALL'))    # '⚽'
print(lookup('BABY').encode())  # b'\xf0\x9f\x91\xb6'

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
suits = ['coin', 'string', 'myriad']
original_suits = suits
suits.pop()
suits.remove('string')
print(suits)    # ['coin']
suits.append('cup')
suits.extend(['sword', 'club'])
print(suits)    # ['coin', 'cup', 'sword', 'club']
suits[2] = 'spade'
suits[0:2] = ['heart', 'diamond']
print(suits)    # ['heart', 'diamond', 'spade', 'club']
print(original_suits)    # ['heart', 'diamond', 'spade', 'club']


numerals = {'I': 1, 'V': 5, 'X': 10}
numerals['X'] = 11  # {'I': 1, 'V': 5, 'X': 11}
numerals['L'] = 50  # {'I': 1, 'V': 5, 'X': 11, 'L': 50}
numerals.pop('X')    # {'I': 1, 'V': 5, 'L': 50}
print(numerals.get('X'))    # None

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
Tuples
"""

(3, 4, 5, 6) # (3, 4, 5, 6)
print(tuple([3, 4, 5, 6])) # (3, 4, 5, 6)
(2,)    # (2,)
(3, 4, 5) + (6, 7, 8)   # (3, 4, 5, 6, 7, 8)
5 in (3, 4, 5, 6)  # True

{(1, 2): 3}    # {(1, 2): 3}
{(1, [2]): 3}  # TypeError: unhashable type: 'list'

s = ([1, 2], 3)
s[0] = 4    # TypeError: 'tuple' object does not support item assignment
s[0][0] = 4 # ([4, 2], 3)

[10] == [10]    # True
a = [10]
b = [10]
a == b  # True
a is b  # False

c = b
c is b  # True
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

s = [2, 3]
t = [5, 6]
s.append(t) # [2, 3, [5, 6]]
s.extend(t) # [2, 3, 5, 6]
t[1] = 0 # [2, 3, 5, 0]

a = s + [t] # [2, 3, 5, 6, [5, 0]]
b = a[1:]   # [3, 5, 6, [5, 0]]
a[1] = 9    # [2, 9, 5, 6, [5, 0]]
b[1][1] = 0 # [3, 5, 6, [5, 0]]
# all the changes above affect a, b, s, and t

t = list(s)
s[1] = 0 # s = [2, 0, 5, 0], t = [2, 3, 5, 0]

s[0:0] = t
s[3:] = t
t[1] = 0