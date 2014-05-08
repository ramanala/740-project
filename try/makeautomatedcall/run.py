#!//usr/bin/python

from flask import Flask
from flask import render_template
from flask import request
from twilio.rest import TwilioRestClient

from datetime import datetime


# Get these credentials from http://twilio.com/user/account
account_sid = "AC3d6188091a9109165c89ae83c5d94d1b"
auth_token = "7a0007278ebe72b311ca4d476c7a6abc"
client = TwilioRestClient(account_sid, auth_token)
 
# Make the call


tostring1 = "client:bamboo"
tostring2 = "7074079806"



call1 = client.calls.create(to=tostring1,  # Any phone number
                           from_ = "+16082345103",
                           url = "http://flask-twilioproject740.rhcloud.com/default",
                           method="GET") # Must be a vsalid Twilio number)
utc_datetime1 = datetime.utcnow()

print "Placed call 1::"+str(utc_datetime1)

'''
for i in range(498):
	call2 = client.calls.create(to=tostring2,  # Any phone number
                           from_ = "+16082345103",
                           url = "http://pages.cs.wisc.edu/~ra/TwimlLibrary/GenericWelcome.xml",
                           method="GET") # Must be a valid Twilio number)
print 'Placed next 298 calls'


call3 = client.calls.create(to=tostring1,  # Any phone number
                           from_ = "+16082345103",
                           url = "http://pages.cs.wisc.edu/~ra/TwimlLibrary/GenericWelcome.xml",
                           method="GET") # Must be a valid Twilio number)
utc_datetime2 = datetime.utcnow()

print "Placed call 2::"+str(utc_datetime2)
'''

print 'Done'