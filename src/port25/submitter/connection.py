# Copyright 2009, NumbersUSA Action
# Peter Halliday <peter@numbersusa.com>

# This software may be freely redistributed under the terms of the GNU
# general public license

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
"""is used to manage the connection to the PowerMTA server."""
from port25 import PmtaError, pmta
from port25.submitter.message import *

class PmtaConnectionError(PmtaError):
    """an error that can get raised at various point.  Each error has a value
    attribute that contain a number of the error and if printed in string 
    contact a human readable representatino too."""
    def __init__(self, conn):
        self.value = pmta.PmtaConnGetLastErrorType(conn)
        pmta.PmtaConnGetLastError.restype = c_char_p
        self.str = pmta.PmtaConnGetLastError(conn)
    def __str__(self):
        return self.str

class Connection(object):
    """"Class that manages the connection to the PowerMTA server.
        
    uri: server to connect to '127.0.0.1', or '1.2.3.4' defaults to '127.0.0.1'
	port: port to connect to defaults to 25"""
    
    def __init__(self, uri="127.0.0.1", port=25):
        self.connection = pmta.PmtaConnAlloc()
        
        #different function are used depending on the URI passed
        if not pmta.PmtaConnConnectRemote(self.connection, uri, port):
            raise PmtaConnectionError(self.connection)
        
    def __del__(self):
        pmta.PmtaConnFree(self.connection)
        
    def submit(self, msg=''):
        """Sending the email over the established connection.  Pass it a 
        Message object.
        
        msg: port25.submitter.message object to send."""
        if not pmta.PmtaConnSubmit(self.connection, msg):
            raise PmtaConnectionError(self.connection)
