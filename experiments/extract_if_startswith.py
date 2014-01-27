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
    if s.startswith(substring):
        return s[len(substring):]
    return False

def test_slice(s, substring):
    l = len(substring)
    return s[l:] if s[:l] == substring else False



if __name__ == '__main__':


    for test_res, part, arg in ((True, "Short strings", '"{0}", "Basic"'.format(short_s)),
                                (True, "Long stack and short needle", str('"{0}", "Basic"'.format(long_s + random_string(10000)))),
                                (True, "Long stack and long needle", str('"{0}ff", "{0}"'.format(long_s + random_string(10000)))),
                                (False, "Short stack and long needle", str('"{0}ff", "{1}"'.format(short_s, long_s + random_string(10000))))
                                ):

        print(part + "\r\n" + "=" * len(part))

        with PrettyTime(test_startswith, None, 2000000) as pt:
            pt(arg)
            assert bool(pt.eval()) == test_res, "Wrong result"


        with PrettyTime(test_slice, None, 2000000) as pt:
            pt(arg)
            assert bool(pt.eval()) == test_res, "Wrong result"

        print("")


# RESULTS
## Short strings
## =============
## Measure test_startswith
## 2000000 loops, best of 3: 0.27 usec per loop
## Measure test_slice
## 2000000 loops, best of 3: 0.203 usec per loop

## Long stack and short needle
## ===========================
## Measure test_startswith
## 2000000 loops, best of 3: 1.13 usec per loop
## Measure test_slice
## 2000000 loops, best of 3: 1.05 usec per loop

## Long stack and long needle
## ==========================
## Measure test_startswith
## 2000000 loops, best of 3: 1.26 usec per loop
## Measure test_slice
## 2000000 loops, best of 3: 1.79 usec per loop

## Short stack and long needle
## ===========================
## Measure test_startswith
## 2000000 loops, best of 3: 0.214 usec per loop
## Measure test_slice
## 2000000 loops, best of 3: 0.161 usec per loop
