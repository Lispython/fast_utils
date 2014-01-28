#!/usr/bin/env python
# -*- coding:  utf-8 -*-
"""
fast-utils
~~~~~~~~~~

fast-utils is a collection of small Python function that can make you scripts more fast.

:copyright: (c) 2014 by Alexandr Lispython, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
:github: http://github.com/Lispython/fast-utils
"""


import os
import sys
from setuptools import  setup, find_packages
from setuptools.command.test import test as BaseTestCommand

try:
    readme_content = open(os.path.join(os.path.abspath(
        os.path.dirname(__file__)), "README.rst")).read()
except Exception as e:
    print(e)
    readme_content = __doc__

VERSION = "0.0.3"


def run_tests():
    from tests import suite
    return suite()

setup_requires = [
    'pytest',
    'nose==1.3.0']

install_require = ["six==1.5.2"]
tests_require = ["nose==1.3.0"] + install_require


class TestCommand(BaseTestCommand):
    def finalize_options(self):
        BaseTestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    name="fast-utils",
    version=VERSION,
    description="fast-utils is a collection of small Python function that can make you scripts more fast.",
    long_description=readme_content,
    author="Alex Lispython",
    author_email="alex@obout.ru",
    maintainer="Alexandr Lispython",
    maintainer_email="alex@obout.ru",
    url="https://github.com/Lispython/fast_utils",
    #packages=['fast_utils'],
    packages=find_packages(exclude=("tests", "tests.*",)),
    #package_dir={'': 'fast_utils'},
    include_package_data=True,
    install_requires=install_require,
    setup_requires=setup_requires,
    cmdclass={'test': TestCommand},
    tests_require=tests_require,
    license="BSD",
    platforms = ['Linux', 'Mac'],
    classifiers=[
        "Environment :: Web Environment",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        #"Programming Language :: Python :: 3.3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Topic :: Utilities",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Development Status :: 5 - Production/Stable"
        ])
