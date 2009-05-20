# Copyright 2009, NumbersUSA Action
# Peter Halliday <peter@numbersusa.com>

# This software may be freely redistributed under the terms of the GNU
# general public license

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
"""Main classes for the port25 python apis."""

from ctypes import *

__docformat__ = 'restructuredtext'
__version__ = '0.0.3'
__license__ = 'GPLv3+'
__author__ = "Peter Halliday"


class PmtaError(Exception):
	pass

pmta = CDLL("libpmta.so")
