#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
fast_utils
~~~~~~~~~~
fast-utils is a collection of small Python function that can make you scripts more fast.

:copyright: (c) 2014 by Alexandr Lispython, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
:github: http://github.com/Lispython/fast_utils
"""

__all__ = 'get_version', 'timeit'
__author__ = "Alexandr Lispython (alex@obout.ru)"
__license__ = "BSD, see LICENSE for more details"
__maintainer__ = "Alexandr Lispython"

try:
    __version__ = __import__('pkg_resources') \
        .get_distribution('fast_utils').version
except Exception, e:
    __version__ = 'unknown'

if __version__ == 'unknown':
    __version_info__ = (0, 0, 0)
else:
    __version_info__ = __version__.split('.')
__build__ = 0x000001

def get_version():
    return __version__
