from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
 

@app.route("/")
def hello():
    return render_template('callmakeinterface.html')

@app.route("/", methods=['POST', 'GET'])
def makecall():    
    phone = ""

    if request.method == 'POST':
    	phone = request.form['phone']
    	
    # Download the library from twilio.com/docs/libraries
	from twilio.rest import TwilioRestClient
	 
	# Get these credentials from http://twilio.com/user/account
	account_sid = "AC3d6188091a9109165c89ae83c5d94d1b"
	auth_token = "7a0007278ebe72b311ca4d476c7a6abc"
	client = TwilioRestClient(account_sid, auth_token)
	 
	# Make the call
	call = client.calls.create(to=phone,  # Any phone number
	                           from_="+16082345103", # Must be a valid Twilio number
	                           url="http://pages.cs.wisc.edu/~ra/response.xml")
	
    return render_template('placedcall.html')

if __name__ == "__main__":
    app.run(debug=True)
