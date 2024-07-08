"""
The class statement
"""
class Clown:
    nose = 'big and red'
    def dance():
        return 'No thanks'
    
Clown.nose
Clown.dance()

class Account:

    interest = 0.02 # A class attribute

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance
    
tom_account = Account('Tom')
tom_account.deposit(100)    # 100

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
attributes
"""
john = Account('John')
john.balance # 0
getattr(john, 'balance') # 0
john.deposit(100) # 100
getattr(john, 'balance') # 100
hasattr(john, 'balance') # True
hasattr(john, 'lance') # False

type(Account.deposit) # 'function'
Account.deposit(tom_account, 1001) # 1001
tom_account.deposit(1000)   # 2011

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
Inheritance
"""
class CheckingAccount(Account):
    """A bank account that charges for withdrawals"""
    withdraw_fee = 1
    interest = 0.01
    def withdraw(self, amount):
        # amount = amount + 1
        # if amount > self.balance:
        #     return 'Insufficient funds'
        # self.balance = self.balance - amount
        # return self.balance
        return Account.withdraw(self, amount + self.withdraw_fee)
    
a = Account('John')
b = CheckingAccount('Jack')
a.balance   # 0 
b.balance   # 0
a.deposit(100)  # 100
b.deposit(100)  # 100
a.withdraw(10)  # 90
b.withdraw(10)  # 89

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Bank:
    """A bank *has* accounts.
    >>> bank = Bank()
    >>> john = bank.open_account('John', 10)
    >>> jack = bank.open_account('Jack', 5, CheckingAccount)
    >>> john.interest
    0.02
    >>> jack.interest
    0.01
    >>> bank.pay_interest()
    >>> john.balance
    10.2
    >>> bank.too_big_to_fail()
    True
    """
    def __init__(self):
        self.accounts = []

    def open_account(self, holder, amount, kind=Account):
        account = kind(holder)
        account = deposit(amount)
        self.accounts.append(account)
        return account
    
    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance * a.interest)

    def too_big_to_fail(self):
        return len(self.accounts) > 1
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
Multiple inheritance
"""
class SavingsAccount(Account):
    deposit_fee = 2
    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_fee)
    
class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1
