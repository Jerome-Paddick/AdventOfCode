from functools import wraps
import functools


def mem():
    memo = {}


def memoize(function):
    print('Im run only once')
    memo = {}
    def wrapper(*args):
        # add the new key to dict if it doesn't exist already
        if args not in memo:
            memo[args] = function(*args)
        return memo[args]
    return wrapper

@memoize
def func1(argument):
    """function 1"""
    print('INSIDE FUNC 1')
    return f'func1 {argument}'


@memoize
def func2(argument):
    """function 2"""
    print('INSIDE FUNC 2')
    return f'func2 {argument}'


print(func1(5))
print(func1(5))
print(func2(5))
