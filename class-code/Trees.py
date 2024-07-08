"""
Slicing
"""
odds = [3, 5, 7, 9]
list(range(1, 2))
[odds[i] for i in range(1, 3)]
odds[1:3]
odds[:3]
odds[1:]
odds[:]

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
Processing Container Values
"""

sum([2, 3, 4])
sum([2, 3, 4], 1)
[2, 3, 4] + [5, 6]
sum([[2, 3, 4], [5, 6]], [])
sum([[2, 3], [4]])  # Error

max(range(5))
max(0, 1, 2, 3, 4)
max(range(10), lambda x: 7-(x-4)*(x-2))

[x < 5 for x in range(10)]  # [True, True, True, True, True, False, False, False, False, False]
all([x < 5 for x in range(10)])  # False
all([x < 5 for x in range(5)])  # True

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
Trees
"""

def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

tree(1) # [1]
is_leaf(tree(1)) # True
tree(1, [5]) # error
t = tree(1, [tree(5, [tree[7]]), tree(6)])
print(t) # [1, [5, [7]], [6]]
print(label(t)) # 1
print(branches(t)) # [[5, [7]], [6]]
print(branches(t)[0]) # [5, [7]]
print(is_tree(branches(t)[0]))  # True
label(branches(t)[0])   # 5

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
Tree Processing
"""

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])
    
def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])
    
def leaves(tree):
    """Return a list containing the leaf labels of tree.
    >>> leaves(fib_tree(5))
    [0, 1, 1, 0, 1]
    """
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])
    
def increment_leaves(t):
    """Return a tree like t but with leaf labels incremented.
    >>> increment_leaves(fib_tree(4))
    [3, [1, [0], 2, [1, [0]], 1, [0, [1, [0]]]]
    """
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)
    
def increment(t):
    """Return a tree like t but with all labels incremented.
    >>> increment(fib_tree(4))
    [4, [1, [0], 3, [1, [0]], 2, [1, [0]]]
    """
    return tree(label(t) + 1, [increment(b) for b in branches(t)])

def print_tree(t, indent=0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

numbers = tree(3, [tree(4), tree(5, [tree(6)])])
haste = tree('h', [tree('a',[tree('s'),
                             tree('t')]),
                             tree('e')])

def print_sum(t, so_far):
    so_far = so_far + label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sum(b, so_far)

print_sum(numbers, 0)   # 7, 4
print_sum(haste, '')    # has, hat, he
