#!/usr/bin/env python

# Copyright 2009, NumbersUSA Action
# Peter Halliday <peter@numbersusa.com>

# This software may be freely redistributed under the terms of the GNU
# general public license

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
"""build script for project."""

__docformat__ = 'restructuredtext'

import os
import sys
from setuptools import Command, setup
from os import path

sys.path.insert(0, 'src')
sys.path.insert(1, 'tests')

from port25 import __author__, __license__, __version__

setup(name='python-port25',
      version=__version__,
      author=__author__,
      author_email='peter@numbersusa.com',
      url='http://python-port25.googlecode.com',
      download_url='http://python-port25.googlecode.com/files/python-port25-%s.tar.gz' % (__version__),
      description="The python API for Port25's PowerMTA.",
      long_description="The python API for Port25's PowerMTA.  It wraps around the C API, but makes it more pythonic.",
      setup_requires=['nose>=0.10'],
      platforms = ['any'],
      license = __license__,
      package_dir={'port25': 'src/port25'},
      packages=['port25', 'port25.submitter'],
      classifiers = [
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Development Status :: 5 - Production/Stable',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Programming Language :: Python'],
      test_suite = 'nose.collector',
      )
