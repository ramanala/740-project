#!//usr/bin/python

from flask import Flask
from flask import render_template
from flask import request
from twilio.rest import TwilioRestClient
import sys
from datetime import datetime


body = sys.argv[1]

body = body * 2048
# Get these credentials from http://twilio.com/user/account
account_sid = "AC7a090d2892a567f91425856c9aa662ec"
auth_token = "935d7ee7ce7bca2061795d7d3374b189"
client = TwilioRestClient(account_sid, auth_token)
 

tostring1 = "client:ram"
tostring2 = "+16085566961"

message = client.messages.create(to=tostring2,  # Any phone number
                           from_ = "+17078404769",
                           body=body) # Must be a valid Twilio number)


print message.sid

attrs = vars(message)
print ', '.join("%s: %s" % item for item in attrs.items())