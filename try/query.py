#!//usr/bin/python

from flask import Flask
from flask import render_template
from flask import request
from twilio.rest import TwilioRestClient
import sys
import os
from datetime import datetime


# Get these credentials from http://twilio.com/user/account
account_sid = "AC7a090d2892a567f91425856c9aa662ec"
auth_token = "935d7ee7ce7bca2061795d7d3374b189"
client = TwilioRestClient(account_sid, auth_token)
 
call = client.calls.get(sys.argv[1])
print call.status
