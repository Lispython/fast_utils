#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
fast_utils.cache
~~~~~~~~~~~~~~~~

Cache and memoization functions

:copyright: (c) 2014 by Alexandr Lispython (alex@obout.ru).
:license: BSD, see LICENSE for more details.
:github: http://github.com/Lispython/fast-utils

"""

__all__ = "memo", "simple_memo", "memo_decorator"

import functools

from fast_utils.exceptions import NotMemoizedError


class memo_decorator(dict):

    __slots__ = ('func', '_missing', '_get', '_resets')

    def __init__(self, func):
        self.func = func
        self.func.cache_info = self.cache_info
        self.func.clear_cache = self.clear_cache
        self._missing = 0
        self._get = 0
        self._resets = 0

    def cache_info(self):
        return {"missing": self._missing,
                "get": self._get,
                "resets": self._resets}

    def clear_cache(self):
        self._missing = 0
        self._get = 0
        self._resets += 1
        return self.clear()

    def __call__(self, *args, **kwargs):

        try:
            key = self.make_key(args, kwargs)
        except NotMemoizedError:
            return self.func(*args, **kwargs)

        try:
            self._get += 1
            return self[key]
        except KeyError:
            self._missing += 1
            self[key] = ret = self.func(*args, **kwargs)
            return ret


    ## def __missing__(self):
    ## missig is more fast instead of catch exception
    ## but I don't have ideas how to use it

    def __get__(self, instance, instancetype):
        """Implement the descriptor protocol to make decorating instance
        method possible.

        """
        # Return a partial function with the first argument is the instance
        #   of the class decorated.
        return functools.partial(self.__call__, instance)

    def to_simple(self, value):
        if isinstance(value, list):
            return tuple((self.to_simple(x) for x in value))
        elif isinstance(value, dict):
            return tuple(sorted((k, self.to_simple(v)) for k, v in value.items()))
        else:
            return value

    def make_key(self, args, kwargs):
        return (self.func.__module__, self.func.func_name,
                self.to_simple(list(args)), self.to_simple(kwargs))


def memo(decorator=None):
    if not decorator:
        return memo_decorator
    return decorator


def simple_memo(f):
    """Simple memoization for one argument functions
    """
    class memodict(dict):
        __slots__ = ()
        def __missing__(self, key):
            self[key] = ret = f(key)
            return ret
    return memodict().__getitem__


class Cache(dict):
    __slots__ = ()

    def __call__(self, f, *args):

        import ipdb; ipdb.set_trace()
        try:
            return self[[f.func_name] + args]
        except IndexError:
            self[[f.func_name] + args] = ret = f(*args)
            return ret

    ## def __missing__(self, key):
    ##     import ipdb; ipdb.set_trace()
    ##     self[key] = ret = key[0](*key[1:])
    ##     return ret
