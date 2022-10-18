from functools import cache

__all__ = ['my_sum', 'factorial']


def my_sum(iterable):
    return sum(iterable)


@cache
def factorial(n):
    return n * factorial(n-1) if n else 1
