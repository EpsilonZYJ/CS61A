def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)
    
def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted

fib = count(fib)
fib(5) # 15

def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
Exponetiation
"""
def exp_fast(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(exp_fast(b, n//2))
    else:
        return b * exp_fast(b, n-1)
    
def square(x):
    return x*x
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def count_frames(f):
    def counted(n):
        counted.open_count += 1
        if counted.open_count > counted.max_count:
            counted.max_count = counted.open_count
        result = f(n)
        return result
    counted.open_count = 0
    counted.max_count = 0
    return counted

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)
 
fib = count_frames(fib)
fib(20)
fib.open_count  # 0
fib.max_count   # 20











