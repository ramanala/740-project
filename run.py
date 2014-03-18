from flask import Flask
from flask import render_template
from flask import request
from twilio.rest import TwilioRestClient

from datetime import datetime


phone = "+17074079806"

# Get these credentials from http://twilio.com/user/account
account_sid = "AC7a090d2892a567f91425856c9aa662ec"
auth_token = "935d7ee7ce7bca2061795d7d3374b189"
client = TwilioRestClient(account_sid, auth_token)
 
# Make the call
tstart = datetime.now()
call1 = client.calls.create(to=phone,  # Any phone number
                           from_="+17078404769",
                           url = "http://pages.cs.wisc.edu/~ra/TwimlLibrary/GenericWelcome.xml") # Must be a valid Twilio number)

tend = datetime.now()

print 'Time difference:' + str(tend-tstart)

print call1.sid
