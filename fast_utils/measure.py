#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
fast_utils.timeit
~~~~~~~~~~~~~~~~~

Timeit helpers for experiments

:copyright: (c) 2014 by Alexandr Lispython (alex@obout.ru).
:license: BSD, see LICENSE for more details.
:github: http://github.com/Lispython/fast_utils
"""

from timeit import Timer, default_number, default_repeat


class PrettyTimer(Timer):

    def pretty_timeit(self, number=default_number):
        t = PrettyTimer.timeit(self, number)
        self.format_timeit(t, number, default_repeat)

    def pretty_repeat(self, repeat=default_repeat, number=default_number):
        t = PrettyTimer.repeat(self, repeat, number)
        self.format_timeit(min(t), number, repeat)

    def format_timeit(self, t, number, repeat):
        precision = 3
        usec = t * 1e6 / number
        if usec < 1000:
            print( "%d loops, best of %d: %.*g usec per loop" % (number, repeat, precision, usec))
        else:
            msec = usec / 1000
            if msec < 1000:
                print("%d loops, best of %d: %.*g msec per loop" % (number, repeat, precision, msec))
            else:
                sec = msec / 1000
                print("%d loops, best of %d: %.*g sec per loop" % (number, repeat, precision, sec))



class PrettyTime(object):


    def __init__(self, f, name=None, number=default_number, repeat=default_repeat):
        self.f = f
        self._code = None
        self._number = number
        self._repeat = repeat
        self._name = name

    def __call__(self, s):
        self._code = s

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        t = PrettyTimer(setup=self.setup, stmt=self.code)

        print("Measure {0}".format(self._name or self.f.func_name))
        t.pretty_repeat(self._repeat, self._number)

    @property
    def code(self):
        return "{0}({1})".format(self._name or self.f.func_name, self._code)

    @property
    def setup(self):

        return "from {0} import {1}".format(self.f.__module__, self._name or self.f.func_name)

    def eval(self):
        return self.f(*eval(self._code))


## def show_results(result):
##     "Print results in terms of microseconds per pass and per item."
##     global count, range_size
##     per_pass = 1000000 * (result / count)
##     print '%.2f usec/pass' % per_pass,
##     per_item = per_pass / range_size
##     print '%.2f usec/item' % per_item
