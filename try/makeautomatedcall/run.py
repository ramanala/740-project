#!//usr/bin/python

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


tostring1 = "client:ram"
tostring2 = "7074079806"


utc_datetime1 = datetime.utcnow()
call1 = client.calls.create(to=tostring1,  # Any phone number
                           from_ = "+17078404769",
                           url = "http://pages.cs.wisc.edu/~ra/TwimlLibrary/GenericWelcome.xml",
                           method="GET") # Must be a valid Twilio number)

print "Placed call 1"

for i in range(1000):
	call2 = client.calls.create(to=tostring2,  # Any phone number
                           from_ = "+17078404769",
                           url = "http://pages.cs.wisc.edu/~ra/TwimlLibrary/GenericWelcome.xml",
                           method="GET") # Must be a valid Twilio number)


print 'Placed next 1000 calls'

utc_datetime2 = datetime.utcnow()
call3 = client.calls.create(to=tostring1,  # Any phone number
                           from_ = "+17078404769",
                           url = "http://pages.cs.wisc.edu/~ra/TwimlLibrary/GenericWelcome.xml",
                           method="GET") # Must be a valid Twilio number)

print 'Placed 101st call to ram'

print 'Time just before queuing call-1:' + str(utc_datetime1)
print 'Time just before queuing call-101:' + str(utc_datetime2)