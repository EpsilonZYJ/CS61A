"""
Linked List Structure
"""
class Link:

    empty = ()
    
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

def square(x):
    return x*x

def odd(x):
    return x%2 == 1

def range_link(start, end):
    if start >= end:
        return Link.empty
    else:
        return Link(start, range_link(start+1, end))
    
def map_link(f, s):
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))
    
def filter_link(f, s):
    if s is Link.empty:
        return s
    filtered_rest = filter_link(f, s.rest)
    if f(s.first):
        return Link(s.first, filtered_rest)
    else:
        return filtered_rest

def add(s, v):
    assert s is not Link.empty
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and s.rest is Link.empty:
        s.rest = Link(v)
    elif s.first < v:
        add(s.rest, v)
    return s
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
Tree class
"""
class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)


def fib_tree(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = left.label + right.label
        return Tree(fib_n, [left, right])
    
def prune(t, n):
    t.branches = [b for b in t.branches if b.label != n]
    for b in t.branches:
        prune(b, n)
