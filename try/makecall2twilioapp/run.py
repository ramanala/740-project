from flask import Flask, request, render_template
from twilio.util import TwilioCapability
import twilio.twiml
 
import re
 
app = Flask(__name__)
 
# Add a Twilio phone number or number verified with Twilio as the caller ID
caller_id = "+17074079806"
 
# put your default Twilio Client name here, for when a phone number isn't given
default_client = "ram"
  
@app.route('/client', methods=['GET', 'POST'])
def client():
    """Respond to incoming requests."""
 
    # Find these values at twilio.com/user/account
    account_sid = "AC7a090d2892a567f91425856c9aa662ec"
    auth_token = "935d7ee7ce7bca2061795d7d3374b189"
 
    capability = TwilioCapability(account_sid, auth_token)
 
    application_sid = "APa102e77aab1e5e82ccd8fb9d0733f533" # Twilio Application Sid
    capability.allow_client_incoming("ram")
    token = capability.generate()
 
    return render_template('client.html', token=token)
 
if __name__ == "__main__":
    app.run(debug=True)