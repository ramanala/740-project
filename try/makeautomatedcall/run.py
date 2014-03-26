from flask import Flask
from flask import render_template
from flask import request
from twilio.rest import TwilioRestClient

from datetime import datetime


# Get these credentials from http://twilio.com/user/account
account_sid = "AC7a090d2892a567f91425856c9aa662ec"
auth_token = "935d7ee7ce7bca2061795d7d3374b189"
client = TwilioRestClient(account_sid, auth_token)
 
# Make the call
utc_datetime1 = datetime.utcnow()
call1 = client.calls.create(to="client:ram",  # Any phone number
                           from_ = "+17078404769",
                           url = "http://flask-twilioproject740.rhcloud.com/default",
                           method="GET") # Must be a valid Twilio number)


utc_datetime2 = datetime.utcnow()

print utc_datetime1
print utc_datetime2

#print call1.sid
