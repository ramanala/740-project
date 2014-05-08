from flask import Flask, request, render_template
from twilio.util import TwilioCapability
import twilio.twiml
import re
import os
from datetime import datetime 

app = Flask(__name__)
 
# Add a Twilio phone number or number verified with Twilio as the caller ID
caller_id = "+16082345103"
 
# put your default Twilio Client name here, for when a phone number isn't given
default_client = "jenny"
 
@app.route('/voice', methods=['GET', 'POST'])
def voice():
    if request is not None:
    	with open('/tmp/iplog', 'w') as fip:
		headers_list = request.headers.getlist("X-Forwarded-For")
		real_ip = request.headers.get('X-Real-IP')
		user_ip = headers_list[0] if headers_list else request.remote_addr
		fip.write(request.method +' request from '+ user_ip )

		dest_number = request.values.get('PhoneNumber', None) 
		resp = twilio.twiml.Response()
			 
		with resp.dial(callerId=caller_id) as r: 
			if dest_number is not None:	
				if dest_number and re.search('^[\d\(\)\- \+]+$', dest_number):
					r.number(dest_number)
				else:
					r.client(dest_number)
				 
				fip.write('\n ' + str(resp))
				return str(resp)
			else:
				#Probably incoming call from phone
				r.client("ram")
				return str(resp)


@app.route('/statuscallback', methods=['GET', 'POST'])
def statuscallback():
    with open('/tmp/statuscallback', 'a') as st:
        st.write('Status Called')
        st.write(request.values.get('MessageSid', None))
        st.write(request.values.get('MessageStatus', None))
    return 'Done'
        
@app.route('/default', methods=['GET', 'POST'])
def default():
    utc_datetime1 = datetime.utcnow()
    xmlreponse = ''
    with open('/tmp/timelog', 'a') as tip:
    	tip.write('Request from Twilio reached at ' + str(utc_datetime1))
    	xmlresponse= '''<Response><Say voice="alice" loop="1">Hey this is a message</Say></Response>'''
    	tip.write('\nGoing to return ' + str(datetime.utcnow()))		
    return xmlresponse
    
@app.route('/client', methods=['GET', 'POST'])
def client():
    """Respond to incoming requests."""
 
    # Find these values at twilio.com/user/account
    account_sid = "AC3d6188091a9109165c89ae83c5d94d1b"
    auth_token = "7a0007278ebe72b311ca4d476c7a6abc"
 
    capability = TwilioCapability(account_sid, auth_token)
    clientName = request.values.get('ClientName', None) 

    application_sid = "APcdc54402e77bd0aa98ab42bd5d045f89" # Twilio Application Sid
    capability.allow_client_incoming(clientName)
    capability.allow_client_outgoing(application_sid)
    token = capability.generate()
 
    return render_template('client.html', token=token)

@app.route('/message', methods=['GET', 'POST'])
def message():
    """Respond to incoming requests."""
    return "<Response><Message>Thanks for your message! We are actively working on your query.</Message></Response>"

if __name__ == "__main__":
    app.run(debug=True)
