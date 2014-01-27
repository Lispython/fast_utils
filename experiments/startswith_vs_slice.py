#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
startswith
~~~~~~~~~~

Check that string startswith by string

:copyright: (c) 2014 by Alexandr Lispython (alex@obout.ru).
:license: BSD, see LICENSE for more details.
:github: http://github.com/Lispython/fast-utils
"""


from fast_utils.measure import PrettyTime
from string import ascii_letters
from random import choice

def random_string(l):
    return ''.join([choice(ascii_letters) for x in xrange(l)])

short_s = "Basic dXNlcm5hbWU6cGFzc3dvcmQ="
long_s = "Basic " + random_string(10000)


def test_startswith(s, substring):
    return s.startswith(substring)

def test_slice(s, substring):
    return s[:len(substring)] == substring

# test_slice more fast on short strings
# but more slow on long strings


if __name__ == '__main__':

    for test_res, part, arg in ((True, "Short strings", '"{0}", "Basic"'.format(short_s)),
                                (True, "Long stack and short needle", str('"{0}", "Basic"'.format(long_s + random_string(10000)))),
                                (True, "Long stack and long needle", str('"{0}ff", "{0}"'.format(long_s + random_string(10000)))),
                                (False, "Short stack and long needle", str('"{0}ff", "{1}"'.format(short_s, long_s + random_string(10000))))
                                ):

        print(part + "\r\n" + "=" * len(part))

        with PrettyTime(test_startswith, None, 20000) as pt:
            pt(arg)
            assert bool(pt.eval()) == test_res, "Wrong result"

        with PrettyTime(test_slice, None, 20000) as pt:
            pt(arg)
            assert bool(pt.eval()) == test_res, "Wrong result"

        print("")


## Short strings
## =============
## Measure test_startswith
## 2000000 loops, best of 3: 0.199 usec per loop
## Measure test_slice
## 2000000 loops, best of 3: 0.159 usec per loop

## Long stack and short needle
## ===========================
## Measure test_startswith
## 2000000 loops, best of 3: 0.208 usec per loop
## Measure test_slice
## 2000000 loops, best of 3: 0.175 usec per loop

## Long stack and long needle
## ==========================
## Measure test_startswith
## 2000000 loops, best of 3: 1.22 usec per loop
## Measure test_slice
## 2000000 loops, best of 3: 1.79 usec per loop

## Short stack and long needle
## ===========================
## Measure test_startswith
## 2000000 loops, best of 3: 0.195 usec per loop
## Measure test_slice
## 2000000 loops, best of 3: 0.135 usec per loop
