"""
Mutable functions
"""

def make_withdraw(balance):
    """Return a withdraw function with a starting balance."""
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw

withdraw = make_withdraw(100)
withdraw(25)  # 75
withdraw(25)  # 50
withdraw(60)  # 'Insufficient funds'
withdraw(15)  # 35

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
Nonlocal statement
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
john = make_withdraw(100)
steven = make_withdraw(1000000)

john is not steven #True
john == steven #False

john(10) #90
steven(1000) #99000
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
Transparency lost
"""
def f(x):
    x = 4
    def g(y):
        def h(z):
            nonlocal x
            x = x + 1
            return x + y + z
        return h
    return g

a = f(1)
b = a(2)
total = b(3) + b(4) #22  total = 10 + b(4) -> 21

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
