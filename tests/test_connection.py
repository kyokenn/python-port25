# Copyright 2009, NumbersUSA Action
# Peter Halliday <peter@numbersusa.com>
        
# This software may be freely redistributed under the terms of the GNU
# general public license
        
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
"""this tests the port25.submitter.connection module."""
import unittest
from port25.submitter.connection import Connection, PmtaConnectionError

class ConnectionTest(unittest.TestCase):
	"""this tests the Connection object in the port25 connection module."""
	
	def test_init_fails(self):
		"""this tests the __init__ function of the Connection object to ensure
		it fails if a hostname that is unroutable is passed."""
		self.assertRaises(PmtaConnectionError, Connection, '127.0.0.1', '5555')
		
	def test_submit_fails(self):
		"""this tests the __init__ function of the Connection object to ensure
		it fails if no message is passed."""
		conn = Connection()
		self.assertRaises(PmtaConnectionError, conn.submit)
