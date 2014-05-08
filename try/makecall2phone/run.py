from flask import Flask, request, render_template
from twilio.util import TwilioCapability
import twilio.twiml
 
import re
 
app = Flask(__name__)
 
# Add a Twilio phone number or number verified with Twilio as the caller ID
caller_id = "+16082345103"
 
# put your default Twilio Client name here, for when a phone number isn't given
default_client = "jenny"
 
@app.route('/voice', methods=['GET', 'POST'])
def voice():
    if request is not None:
        with open('/tmp/f','a') as fip:
            fip.write(request.remote_addr)

    dest_number = request.values.get('PhoneNumber', None)
    resp = twilio.twiml.Response()
 
    with resp.dial(callerId=caller_id) as r: 
        # If we have a number, and it looks like a phone number:
        if dest_number and re.search('^[\d\(\)\- \+]+$', dest_number):
            r.number(dest_number)
        else:
            r.client(default_client)
 
    return str(resp)
 
@app.route('/client', methods=['GET', 'POST'])
def client():
    """Respond to incoming requests."""
 
    # Find these values at twilio.com/user/account
    account_sid = "AC3d6188091a9109165c89ae83c5d94d1b"
    auth_token = "7a0007278ebe72b311ca4d476c7a6abc"
 
    capability = TwilioCapability(account_sid, auth_token)
 
    application_sid = "APcdc54402e77bd0aa98ab42bd5d045f89" # Twilio Application Sid
    capability.allow_client_outgoing(application_sid)
    token = capability.generate()
 
    return render_template('client.html', token=token)

if __name__ == "__main__":
    app.run(debug=True)