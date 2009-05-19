# Copyright 2009, NumbersUSA Action
# Peter Halliday <peter@numbersusa.com>

# This software may be freely redistributed under the terms of the GNU
# general public license

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
"""is used to manage the message sent to the PowerMTA server."""
from ctypes import c_char_p, c_void_p
from port25 import PmtaError, pmta
from port25.submitter.recipient import *

#: for setReturnType return headers
ReturnHeaders = 0
#: for setReturnType return full
ReturnFull = 1

#: 7-bit encoding
Encoding7Bit = 0
#: 8-bit encoding
Encoding8Bit = 1
#: 64-bit encoding
Encoding64Bit = 2

class PmtaMessageError(PmtaError):
    """an error that can get raised at various point.  Each error has a value
    attribute that contain a number of the error and if printed in string 
    contact a human readable representatino too."""
    def __init__(self, msg):
        self.value = pmta.PmtaMsgGetLastErrorType(msg)
        pmta.PmtaMsgGetLastError.restype = c_char_p
        self.str = pmta.PmtaMsgGetLastError(msg)
    def __str__(self):
        return self.str

class Message(object):
    """Class that manages the message sent to the PowerMTA server.
        
    originator: the string of the email address of who is sending the message."""
    
    def __init__(self, originator):
        #pmta.PmtaMsgAlloc.restype = c_void_p
        self.message = pmta.PmtaMsgAlloc()
        self._as_parameter_ = self.message
        
        if not pmta.PmtaMsgInit(self.message, originator):
            raise PmtaMessageError(self.message)

    def __del__(self):
        pmta.PmtaMsgFree(self.message)

    def addData(self, data):
        """adds data to the message.

        data: a string of everything (headers included) to send."""
        if not pmta.PmtaMsgAddData(self.message, data, len(data)):
            raise PmtaMessageError(self.message)

    def addMergeData(self, data):
	    """adds the mergemail data to the message.

	    data: is the mergemail data to add."""
	    if not pmta.PmtaMsgAddMergeData(self.message, data, len(data)):
		    raise PmtaMessageError(self.message)
				        
    def addRecipient(self, recipient):
        """adds a recipient to the message.
        
        recipient: a recipient of type Recipient object."""
        if not pmta.PmtaMsgAddRecipient(self.message, recipient):
            raise PmtaMessageError(self.message)
        
    def addDateHeader(self):
        """adds date header to the message."""
        if not pmta.PmtaMsgAddDateHeader(self.message):
            raise PmtaMessageError(self.message)        

    def setEncoding(self, encoding=Encoding7Bit):
        """sets the encoding of the message.

        encoding: encoding with default Encoding7Bit (Encoding7Bit, Encoding8Bit, Encoding64Bit)."""
        if not pmta.PmtaMsgSetEncoding(self.message, encoding):
            raise PmtaMessageError(self.message)

    def setEnvelopeId(self, envid):
	    """sets the envelopeID for the message.
	
	    envid: envelope ID to put on the message."""
	    if not pmta.PmtaMsgSetEnvelopeId(self.message, envid):
		    raise PmtaMessageError(self.message)

    def setJobId(self, jobID):
        """sets the jobID of the message

        jobID: the job to set this message to"""
        if not pmta.PmtaMsgSetJobId(self.message, jobID):
            raise PmtaMessageError(self.message)

    def setReturnType(self, type=ReturnHeaders):
        """sets the return type of the message.

        type: type to set the Return to default ReturnHeaders (ReturnHeaders, ReturnFull)."""
        if not pmta.PmtaMsgSetReturnType(self.message, type):
            raise PmtaMessageError(self.message)

	def setVerp(self, is_verp=True):
		"""sets the VERP for the message.
		
		is_verp: whether VERP is set defaults to True (True, False)."""
		if not pmta.PmtaMsgSetVerp(self.message, is_verp):
		    raise PmtaMessageError(self.message)

    def setVirtualMta(self, vmta):
        """sets which virtual MTA is used for this message

        vmta: the vmta to set for this message."""
        if not pmta.PmtaMsgSetVirtualMta(self.message, vmta):
            raise PmtaMessageError(self.message)	
