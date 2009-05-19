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
from distutils.core import Command, setup
from glob import glob
from os.path import basename, walk, splitext
from os.path import join as pjoin
from os import path
from unittest import TextTestRunner, TestLoader

sys.path.insert(0, 'src')
sys.path.insert(1, 'test')

from port25 import __author__, __license__, __version__

class SetupBuildCommand(Command):
    """Master setup build command to subclass from."""
    user_options = []
    
    def initialize_options(self):
        """Setup the current dir."""
        self._dir = os.getcwd()
        
    def finalize_options(self):
        """Seems to be required."""
        pass


class RPMBuildCommand(SetupBuildCommand):
    """Creates an RPM based off spec files."""

    description = "Build an rpm based off of the top level spec file(s)"

    def run(self):
        """Run the RPMBuildCommand."""
        try:
            if os.system('./setup.py sdist'):
                raise Exception("Couldn't call ./setup.py sdist!")
                sys.exit(1)
            if not os.access('dist/rpms/', os.F_OK):
                os.mkdir('dist/rpms/')
            dist_path = os.path.join(os.getcwd(), 'dist')
            rpm_cmd = ('rpmbuild -ba --define "_rpmdir %s/rpms/" '
                '--define "_srcrpmdir %s/rpms/" '
                '--define "_sourcedir %s" *spec' % (
                      dist_path, dist_path, dist_path))
            if os.system(rpm_cmd):
                raise Exception("Could not create the rpms!")
        except Exception, ex:
            print >> sys.stderr, str(ex)

class SphinxCommand(SetupBuildCommand):
    """Creates HTML documentation using Sphinx."""

    description = "Generate documentation via sphinx"

    def run(self):
        """Run the DocCommand."""
        print "Creating html documentation ..."

        try:
            from sphinx.application import Sphinx

            if not os.access(path.join('docs', 'html'), os.F_OK):
                os.mkdir(path.join('docs', 'html'))
            buildername = 'html'
            outdir = path.abspath(path.join('docs', 'html'))
            doctreedir = os.path.join(outdir, '.doctrees')

            confdir = path.abspath('docs')
            srcdir = path.abspath('docs')
            freshenv = False

            # Create the builder
            app = Sphinx(srcdir, confdir, outdir, doctreedir, buildername,
                         {}, sys.stdout, sys.stderr, freshenv)

            # And build!
            app.builder.build_all()
            print "Your docs are now in %s" % outdir
        except ImportError, ie:
            print >> sys.stderr, "You don't seem to have the following which"
            print >> sys.stderr, "are required to make documentation:"
            print >> sys.stderr, "\tsphinx.application.Sphinx"
        except Exception, ex:
            print >> sys.stderr, "FAIL! exiting ... (%s)" % ex

class TestCommand(SetupBuildCommand):
    """Distutils testing command."""

    def run(self):
        """Finds all the tests modules in tests/, and runs them."""
        testfiles = []
        for t in glob(pjoin(self._dir, 'tests', '*.py')):
            if not t.endswith('__init__.py'):
                testfiles.append('.'.join(
                    ['tests', splitext(basename(t))[0]]))

        tests = TestLoader().loadTestsFromNames(testfiles)
        t = TextTestRunner(verbosity = 2)
        t.run(tests)


setup(name='port25',
      version=__version__,
      author=__author__,
      author_email='peter@numbersusa.com',
      description="The python API for Port25's PowerMTA.",
      long_description="The python API for Port25's PowerMTA.  It wraps around the C API, but makes it more pythonic.",
      platforms = ['any'],
      license = __license__,
      package_dir={'port25': 'src/port25'},
      packages=['port25', 'port25.submitter'],
      classifiers = [
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Development Status :: 5 - Production/Stable',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Programming Language :: Python'],
      cmdclass = {'test': TestCommand,
                  'doc': SphinxCommand,
                  'rpm': RPMBuildCommand},
      )

