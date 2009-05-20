Requirements
============
- python 2.3+
- python-setuptools 
- PowerMTA C API

Installation
============
Use the RPM ... or
- Become root (or root like) user
- run python setup.py install

RPM
===
To create a rpm file ...
- python setup.py bdist_rpm
- rpm -ivh dist/python-port25-[version]-[release].rpm
