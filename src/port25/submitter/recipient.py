# Copyright 2009, NumbersUSA Action
# Peter Halliday <peter@numbersusa.com>

# This software may be freely redistributed under the terms of the GNU
# general public license

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
"""port25.submitter.recipient is used to manage the recipient to the 
PowerMTA server."""
from port25 import PmtaError, pmta
from ctypes import c_char_p, c_void_p

#: no notification is desired
NotifyNever = 0
#: notification in case the delivery is successful
NotifySuccess = 1
#: notification in case of a delivery failure
NotifyFailure = 2
#: notification in case of a delay in delivery
NotifyDelay = 4

class PmtaRecipientError(PmtaError):
    """an error that can get raised at various point.  Each error has a value
    attribute that contain a number of the error and if printed in string 
    contact a human readable representatino too."""
    def __init__(self, rcpt):
        self.value = pmta.PmtaRcptGetLastErrorType(rcpt)
        pmta.PmtaRcptGetLastError.restype = c_char_p
        self.str = pmta.PmtaRcptGetLastError(rcpt)
    def __str__(self):
        return self.str

class Recipient(object):
    """Class that manages the recipient to the PowerMTA server.  Doesn't 
    require anything to be passed."""

    def __init__(self, address=''):
        self.recipient = pmta.PmtaRcptAlloc()
        self._as_parameter_ = self.recipient
        if not pmta.PmtaRcptInit(self.recipient, address):
            raise PmtaRecipientError(self.recipient)
        
    def __del__(self):
        pmta.PmtaRcptFree(self.recipient)
        
    def setNotify(self, notify_when=NotifyNever):
        """allows you to set when the receipient is sent a notification.
        
        notify_when: a bitstring of flags.  NotifyNever by default 
        (NotifyNever, NotifySuccess, NotifyFailure, NotifyDelay)"""
        if not pmta.PmtaRcptSetNotify(self.recipient, notify_when):
            raise PmtaRecipientError(self.recipient)
    
    def defineVariables(self, variables=()):
        """similar to defineVariable, but in a more pythonic way.
        
        variables: dictionary of variables to set for the particular recipient."""
        for key in variables.keys():
            if not pmta.PmtaRcptDefineVariable(self.recipient, key, variables[key]):
                raise PmtaRecipientError(self.recipient)
    
    def defineVariable(self, name='', value=''):
        """used to bind mailmerge variable to a recipient.
        
        name: string for mailmerge variable's name
        value: string for mailmerge variable's value"""
        if not pmta.PmtaRcptDefineVariable(self.recipient, c_char_p(name), c_char_p(value)):
            raise PmtaRecipientError(self.recipient)
