# Introduction #

How to access the documentation of the system.


# Details #

Because this is similar to the other Port25 PowerMTA APIs many of the calls are very similar, so the documentation in the User's Guide is helpful.  However, the best documentation to use is the one from the package in terms of the Python API.  It documents both the API as well as the tests.  To access the documentation run

python setup.py build\_sphinx

This command will create an html directory inside of the docs directory.  Open these in a browser.  Also, the documentation is available via pydoc as well once the package is installed.