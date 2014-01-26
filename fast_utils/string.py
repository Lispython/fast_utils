#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
fast_utils.string
~~~~~~~~~~~~~~~~~

fast utils for manipulate with strings

:copyright: (c) 2014 by Alexandr Lispython (alex@obout.ru).
:license: BSD, see LICENSE for more details.
:github: http://github.com/Lispython/fast-utils
"""

def startswith(s, substring):
    """Test that s starts with substring

    :param s: stack string
    :param subsrting: needle string
    return: bool result
    """
    return s[:len(substring)] == substring


def extract_if_startswith(s, substring):
    """Extra string after substring

    :param s: stack string
    :param substring: needle string
    :return: bool result
    """
    l = len(substring)
    return s[l:] if s[:l] == substring else False
