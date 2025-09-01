from flask import *
from dotenv import load_dotenv
from markupsafe import escape
import googlemaps
import requests
import os

from censusAcsCall import acsCallWithTiger

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
CENSUS_API_KEY = os.getenv('CENSUS_API_KEY')

# Need to create an instance of the Flask class. This instance will be the WSGI application.
# The first argument is the name of the application's package. '__name__' is a shortcut for this. 
# This is needed so that Flask knows where to look for resources such as templates and static files.
app = Flask(__name__)

gmaps = googlemaps.Client(GOOGLE_API_KEY)

@app.route('/')
def home():
    return '<h>Home Page</h>'

# Setting up an API 
@app.route('/analyze-location', methods=['GET'])
def analyze_location():     
    error = None

    if request.method == 'GET': 

        # Parameters (arguments passed in the url), formatting it into object. 
        address = request.args.get('address', 'Invalid Address')
        city = request.args.get('city', 'Invalid City')
        state = request.args.get('state', 'Invalid State')
        zipCode = request.args.get('zip', 'Invalid ZIP')
        business_type = request.args.get('business_type', 'Unspecified')
        radius = request.args.get('radius', '1')

        business = {
            'address' : str(address),
            'business_type' : str(business_type),
            'radius' : str(radius)
        }

        # Geocoding address via Google Mas Geocoding service. 
        # Universities, PO boxes, rural areas don't work too well with Google's geocoding service.
        # Instead let user input lat or long, place a pin on a map, or integrate places API to more accurately search places. 
        gLocation = gmaps.geocode(address=business['address'], 
                                  components= {'country' : 'US', 'administrative_area': f'{state}', 
                                               'locality' : f'{city}', 'postal_code' : f'{zipCode}'})
        latLon = gLocation[0]['geometry']['location']
        lat = latLon['lat']
        lon = latLon['lng']

        # Retrieving all tracts w/ ACS data within a mile radius of the address. 
        tracts = acsCallWithTiger(lat, lon, 1)

        # Iterating through all tracts to retrieve data on total population and median income. 
        populationAbrev, medianIncomeAbrev = "B01003_001E", "B19013_001E"
        totalPopulation, totalIncome = 0, 0
 
        for tract in tracts:
            totalPopulation += int(tract[populationAbrev])
            totalIncome += int(tract[medianIncomeAbrev]) * int(tract[populationAbrev])
            
        medianIncome = totalIncome / totalPopulation

        businessInfo = {
            'Address' : business['address'],
            'lat' : lat, 
            'lon' : lon,
            'Population' : totalPopulation, 
            'Median Income' : medianIncome
        }
        
        return businessInfo
    
    return error


# Can mark sections with <> that accepts variables 
# Can specify data type with a format such as <int:userId>
@app.route('/user/<string:username>')
def user(username): 
    return f'{username}'

# Rendering HTML templates with Jinja
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None): 
    return render_template('hello.html', person=name)


with app.test_request_context():
    print(url_for('home'))
    # print(url_for('user', username='pierrot'))
    # print(url_for('static', filename='style.css'))

    


# 13893,  1841
# 18241, 7628

# 9469

# 2701.13137607 + 14694.513465


