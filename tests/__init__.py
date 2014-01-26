#!/usr/bin/env python
# -*- coding:  utf-8 -*-
"""
fast_utils.tests
~~~~~~~~~~~~~~~~

Tests for fast utils.

:copyright: (c) 2014 by Alexandr Lispython, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
:github: http://github.com/Lispython/fast-utils
"""

from fast_utils.string import startswith, extract_if_startswith


def test_startswith():
    assert startswith("Basic ejfknwejklfnwejfnl", "Basic")

def test_extract_if_startswith():
    assert extract_if_startswith("Basic ejfknwejklfnwejfnl", "Basic ") == "ejfknwejklfnwejfnl"
