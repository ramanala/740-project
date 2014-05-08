#!//usr/bin/python

from flask import Flask
from flask import render_template
from flask import request
from twilio.rest import TwilioRestClient
import sys
import os
from datetime import datetime


# Get these credentials from http://twilio.com/user/account
account_sid = "AC3d6188091a9109165c89ae83c5d94d1b"
auth_token = "7a0007278ebe72b311ca4d476c7a6abc"
client = TwilioRestClient(account_sid, auth_token)
 
call = client.calls.get(sys.argv[1])
print call.status
