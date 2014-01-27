#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
memoization
~~~~~~~~~~~

Functions results memoization

:copyright: (c) 2014 by Alexandr Lispython (alex@obout.ru).
:license: BSD, see LICENSE for more details.
:github: http://github.com/Lispython/fast-python
"""

from fast_utils.measure import PrettyTime, PrettyTimer
from fast_utils.cache import memo


def fib1(n):
    return n if n < 2 else fib1(n-2) + fib1(n-1)


# http://code.activestate.com/recipes/578231-probably-the-fastest-memoization-decorator-in-the-/#c8
def memoize1(f):
    """Found on http://code.activestate.com/recipes/578231-probably-the-fastest-memoization-decorator-in-the-/#c8
    """
    class memodict(dict):
        __slots__ = ()
        def __missing__(self, key):
            self[key] = ret = f(key)
            return ret
    return memodict().__getitem__


@memoize1
def fib2(n):
    return n if n < 2 else fib2(n-2) + fib2(n-1)


def memoize2(f):
    """Memoization decorator for functions taking one or more arguments.

    :url: http://code.activestate.com/recipes/578231-probably-the-fastest-memoization-decorator-in-the-/#c1
    """
    class memodict(dict):

        def __init__(self, f):
            self.f = f

        def __call__(self, *args):
            return self[args]

        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)


@memoize2
def fib3(n):
    return n if n < 2 else fib3(n-2) + fib3(n-1)


def memoize3(f):
    """Memoization decorator for functions taking one or more arguments.
    """

    class memodict(dict):
        __slots__ = ('f')

        def __init__(self, f):
            self.f = f

        def __call__(self, *args):
            return self[args]

        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)

@memoize3
def fib4(n):
    return n if n < 2 else fib4(n-2) + fib4(n-1)

class NotMemoizedError(Exception):
    """Exception raise for non cached data"""


@memo()
def fib5(n):
    return n if n < 2 else fib4(n-2) + fib4(n-1)


if __name__ == '__main__':

    import sys
    sys.setrecursionlimit(10000)

    for test_res, part, arg in ((55, "x==10", "10"),
                                #(55, "x==100", "1000"),
                                ):

        print(part + "\r\n" + "=" * len(part))

        for x in [ "fib2", "fib3", "fib4", "fib5"]:
            print("Measure {0}".format(x))

            PrettyTimer(setup="from __main__ import {0}".format(x),
                        stmt="{0}({1})".format(x, arg),).pretty_repeat(number=10)

        print("")
