from ctypes import *

class PmtaError(Exception):
	pass

pmta = CDLL("libpmta.so")
