# Download the library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
 
# Get these credentials from http://twilio.com/user/account
account_sid = "AC7a090d2892a567f91425856c9aa662ec"
auth_token = "935d7ee7ce7bca2061795d7d3374b189"
client = TwilioRestClient(account_sid, auth_token)
 
# Make the call
call = client.calls.create(to="+17074079806",  # Any phone number
                           from_="+17078404769", # Must be a valid Twilio number
                           url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
print call.sid