from port25.submitter.message import Message, PmtaMessageError
from port25.submitter.recipient import Recipient, PmtaRecipientError
from port25.submitter.connection import Connection, PmtaConnectionError
from port25 import PmtaError

try:

	list = ('peter@numbersusa.com', 'rich@numbersusa.com',)
	list_data = {'peter@numbersusa.com': {'name': 'Peter'}, 'rich@numbersusa.com': {'name': 'Rich'},}
	data = "From: roybeck@numbersusa.com\12To:[*to]\12Subject: Your Order has been processed\12Mime-Version: 1.0\12Content-type: multipart/alternative;boundary=\"PMTAMimeBoundry\"\12[name]<br><br>Hey your order of a [order] has come in.  Please stop by and give us your money.<br><br>Tech Team <br>"

	msg = Message('roy@numbersusa.com')

        rcpt = None
	for item in list:
		rcpt = Recipient(item)
		rcpt.defineVariable('name', list_data[item]['name'])
		rcpt.defineVariable('order', 'pizzas')
		rcpt.defineVariable('*parts', '1')
		msg.addRecipient(rcpt)

	msg.addMergeData(data) 
	conn = Connection()
	conn.submit(msg)
	
except PmtaError, e:
        print e 
except Exception, e:
        print "Some other error"
        print e.args
	
