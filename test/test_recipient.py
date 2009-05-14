"""this tests the port25.submitter.recipient module."""
import unittest
from port25.submitter.recipient import Recipient, PmtaRecipientError

class RecipientTest(unittest.TestCase):
	"""this tests the Recipient object in the port25 recipient module."""
	
	def test_init_fails(self):
		"""this tests the __init__ function of the Recipient object to ensure
		it fails if no recipient email is passed."""
		self.assertRaises(PmtaRecipientError, Recipient())
		
	def test_empty_variables_fail(self):
		"""this tests the defineVariable function of the Recipient object to ensure
		it fails if no variables are passed."""
		rcpt = Recipient('pedro@pedro.com')
		self.assertRaises(PmtaRecipientError, rcpt.defineVariable())
		
	def test_set_default_variables_fail(self):
		"""this tests the defineVariable function of the Recipient object to ensure
		it fails if you set default variables."""
		rcpt = Recipient('pedro@pedro.com')
		self.assertRaises(PmtaRecipientError, rcpt.defineVariable('*to', 'pedrowski@pedrowski.com'))
		
	def test_set_group_variables_fail(self):
		"""this test ensure if there's at least one data problem in the dictionary
		passed to the setVariables function at least one error is raised."""
		data = {'order': 'pizza', '*to': 'pedrowski@pedrowski.com',}
		rcpt = Recipient('pedro@pedro.com')
		self.assertRaises(PmtaRecipientError, rcpt.defineVariables(data))