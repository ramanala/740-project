from datetime import datetime
# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC3d6188091a9109165c89ae83c5d94d1b"
auth_token = "7a0007278ebe72b311ca4d476c7a6abc"
client = TwilioRestClient(account_sid, auth_token)
 
dt1 = datetime.now()

calls = client.calls.list()

dt2 = datetime.now()


print dt1
print dt2
