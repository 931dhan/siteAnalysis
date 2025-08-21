from flask import *
from dotenv import load_dotenv
from markupsafe import escape
import os


# Need to create an instance of the Flask class. This instance will be the WSGI application.
# The first argument is the name of the application's package. "__name__" is a shortcut for this. 
# This is needed so that Flask knows where to look for resources such as templates and static files.
app = Flask(__name__)

@app.route("/")
def home():
    return '<h>Home Page</h>'

# Setting up an API 
@app.route("/analyze-location", methods=['GET'])
def analyze_location(): 
    error = None

    if request.method == 'GET': 


        # Parameters (arguments passed in the url)
        address = request.args.get('address', 'Invalid Address')
        business_type = request.args.get('business_type', 'Unspecified')
        radius = request.args.get('radius', '1')

        business = {
            'address' : str(address),
            'business_type' : str(business_type),
            'radius' : str(radius)
        }


        # Form data, data received from PUT or POST requests via the body
        return  business 
    
    return error

# Can mark sections with <> that accepts variables 
# Can specify data type with a format such as <int:userId>
@app.route("/user/<string:username>")
def user(username): 
    return f' {username}'

# Rendering HTML templates with Jinja
@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None): 
    return render_template('hello.html', person=name)


with app.test_request_context():
    print(url_for('home'))
    print(url_for('user', username='pierrot'))
    print(url_for('static', filename='style.css'))