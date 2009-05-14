from distutils.core import setup
setup(name='port25',
      version='0.1',
      author='Peter Halliday',
      author_email='peter@numbersusa.com',
      description="The python API for Port25's PowerMTA.",
      long_description="The python API for Port25's PowerMTA.  It wraps around the C API, but makes it more pythonic."
      package_dir={'port25': 'src'},
      packages=['port25', 'port25.submitter'],
      )
