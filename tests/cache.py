#!/usr/bin/env python
# -*- coding:  utf-8 -*-
"""
fast_utils.cache
~~~~~~~~~~~~~~~~

Cache tests for fast utils.

:copyright: (c) 2014 by Alexandr Lispython, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
:github: http://github.com/Lispython/fast-utils
"""


from fast_utils.cache import memo


def test_fib():

    @memo()
    def fib(n):
        return n if n < 2 else fib(n-2) + fib(n-1)

    assert fib == {}
    assert fib(10) == 55
    assert fib.cache_info() == {'get': 19, 'missing': 11, 'resets': 0}

    fib.clear_cache()
    assert fib.cache_info() == {'get': 0, 'missing': 0, 'resets': 1}
