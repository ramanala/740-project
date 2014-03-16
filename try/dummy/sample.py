from datetime import datetime
# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC7a090d2892a567f91425856c9aa662ec"
auth_token = "935d7ee7ce7bca2061795d7d3374b189"
client = TwilioRestClient(account_sid, auth_token)
 
dt1 = datetime.now()

calls = client.calls.list()

dt2 = datetime.now()


print dt1
print dt2
#for call in calls:
	#print call.sid + '--' + call.status