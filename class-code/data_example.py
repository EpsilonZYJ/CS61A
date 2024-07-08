class Worker:
    greeting = 'Sir'
    def __init__(self):
        self.elf = Worker
    def work(self):
        return self.greeting + ', I work'
    def __repr__(self):
        return Bourgeoisie.greeting
    
class Bourgeoisie(Worker):
    greeting = 'Peon'
    def work(self):
        print(Worker.wor(self))
        return 'I gather wealth'
    
jack = Worker()
john = Bourgeoisie()
jack.greeting = 'Maam'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def min_abs_indices(s):
    """
    >>> min_abs_indices([-4, -3, -2, 3, 2, 4])
    6
    >>> min_abs_indices([1, 2, 3, 4, 5])
    [0]
    """
    min_abs = min(map(abs, s))
    return [i for i in range(len(s)) if abs(s[i]) == min_abs]


def largest_adj_sum(s):
    """
    >>> largest_adj_sum([-4, -3, -2, 3, 2, 4])
    6
    >>> largest_adj_sum([-4, -3, -2, 3, 2, -4])
    1
    """
    return max([s[i]+s[i+1] for i in range(len(s)-1)])


def digit_dict(s):
    """
    >>> digit_dict([5, 8, 13, 21, 34, 55, 89])
    {1:[21], 3:[13], 4:[34], 5:[5, 55], 8:[8], 9:[89]} 
    """
    return {d:[x for x in s if x%10 == d] for d in range(10) if any([x%10 == d for x in s])}


def all_have_an_equal(s):
    """
    >>> all_have_an_equal([-4, -3, -2, 3, 2, 4])
    False
    >>> all_have_an_equal([4, 3, 2, 3, 2, 4])
    True
    """
    return all([s[i] in s[:i] + s[i+1:] for i in range(len(s))])










