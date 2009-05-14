"""this tests the port25.submitter.connection module."""
import unittest
from port25.submitter.connection import Connection, PmtaConnectError

class ConnectionTest(unittest.TestCase):
	"""this tests the Connection object in the port25 connection module."""
	
	def test_init_fails(self):
		"""this tests the __init__ function of the Connection object to ensure
		it fails if a hostname that is unroutable is passed."""
		self.assertRaises(PmtaConnectError, Connection('111.111.111.111'))
		
	def test_submit_fails(self):
		"""this tests the __init__ function of the Connection object to ensure
		it fails if no message is passed."""
		conn = Connection()
		self.assertRaises(PmtaConnectError, conn.submit())