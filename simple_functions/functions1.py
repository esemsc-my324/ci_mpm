from functools import cache


"""
When from module import * is used,
only the names listed in __all__ will be imported.
"""

__all__ = ["my_sum", "factorial"]


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@cache
def factorial(n):
    return n * factorial(n - 1) if n else 1
