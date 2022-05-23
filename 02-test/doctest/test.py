# python -m doctest -v test.py
from numba import jit

@jit
def foo(x):
    """
    >>> foo(2)
    4
    """
    return x*x
