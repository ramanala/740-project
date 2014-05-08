#!//usr/bin/python

from flask import Flask
from flask import render_template
from flask import request
from twilio.rest import TwilioRestClient
import sys
from datetime import datetime
import numpy
 
body = sys.argv[1] * 100
count = int(sys.argv[2])

# Get these credentials from http://twilio.com/user/account
account_sid = "AC3d6188091a9109165c89ae83c5d94d1b"
auth_token = "7a0007278ebe72b311ca4d476c7a6abc"
client = TwilioRestClient(account_sid, auth_token)
 
tostring1 = "+16085566961"
tostring2 = "+17074079806"


for i in range(count):
	if i%2 == 0:
		message = client.messages.create(to=tostring1,  # Any phone number
			                           from_ = "+16082345103",
			                           media="https://demo.twilio.com/owl.png",
			                           StatusCallback="http://flask-twilioproject740.rhcloud.com/statuscallback",
			                           body=body) # Must be a valid Twilio number)
	else:
		message = client.messages.create(to=tostring2,  # Any phone number
			                           from_ = "+16082345103",
			                           media="https://demo.twilio.com/owl.png",
			                           StatusCallback="http://flask-twilioproject740.rhcloud.com/statuscallback",
			                           body=body) # Must be a valid Twilio number)


print 'Done'