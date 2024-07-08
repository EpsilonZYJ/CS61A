digits = [1, 8, 2, 8]
print(len(digits))
print(digits[3])
#print(getitem(digits, 3))
[2, 7] + digits * 2
print(1 in digits) #True
print(not(5 in digits))
print(5 not in digits)

def count(s, value):
    """Count the number of times that value appears
    in sequence s
    """
    total, index = 0, 0
    for element in s:
        if element == value:
            total += 1
    return total

count([1, 2, 1, 2, 1], 1)

pairs = [[1, 2], [2, 2], [3, 2], [4, 4]]
same_count = 0
for x, y in pairs:
    if x == y:
        same_count += 1
print(same_count)

list(range(-2, 2))#[-2,-1,0,1]
list(range(4)) #[0,1,2,3]

def sum_below(n):
    total = 0
    for i in range(n):
        total += i
    return total

def cheer():
    for _ in range(3):
        print("Go Bears!")

def mysum(L):
    if(L == []):
        return 0
    else:
        return L[0] + mysum(L[1:])
    
def sum_iter(n):
    sum = 0
    for i in range(0, n+1):
        sum = sum + i
    return sum
    
print(mysum([2, 4, 1, 5]))

""""""""""""""""""""""""""""""""""""""""""

"""
List Comprehensions
"""

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'm', 'n', 'o', 'p']
[letters[i] for i in [3, 4, 6, 8]]

odds = [1, 3, 5, 7, 9]
[x+1 for x in odds]
[x+1 for x in odds if 25 % x == 0]

def divisors(n):
    return [1] + [x for x in range(2, n) if n%x==0]

""""""""""""""""""""""""""""""""""""""""""""

"""
Strings
"""

print('curry = lambda f: lambda x: lambda y: f(x, y)')
exec('curry = lambda f: lambda x: lambda y: f(x, y)')

from operator import add
print(curry(add)(3)(4))

""""""""""""""""""""""""""""""""""""""""""""

city = 'Berkeley'
len(city)   #8
city[3]    #'k'


'here' in "Where's Waldo?" #True
234 in [1, 2, 3, 4] #False
[2, 3, 4] in [1, 2, 3, 4] #False


def reverse(s):
    if len(s) == 1:
        return s
    else:
        return reverse(s[1:]) + s[0]