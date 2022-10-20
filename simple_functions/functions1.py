from functools import cache

__all__ = ['my_sum', 'factorial']


def my_sum(iterable):
    '''docstring of function my_sum'''
    return sum(iterable)


@cache
def factorial(n):
    '''docstring of function factorial'''
    return n * factorial(n-1) if n else 1
