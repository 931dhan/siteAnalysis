import requests
import os 
from dotenv import load_dotenv
from censusGeocode import censusGeocode
from tigerTractQuery import tigerTractQuery
from collections import defaultdict 


load_dotenv()
CENSUS_API_KEY = os.getenv('CENSUS_API_KEY')


def acsCall(lat, lon): 

    # Base URL for API calls to Census ACS API 
    # Example of a call
    # https://api.census.gov/data/2023/acs/acs5?get=NAME,B01001_001E&for=metropolitan%20division:*&in=metropolitan%20statistical%20area/micropolitan%20statistical%20area:3562
    url = 'https://api.census.gov/data/2023/acs/acs5'

    # Find the tract, state, and county of address. 
    geo = censusGeocode(lat, lon)

    #  Variables correspond to a different demographic variables, such as median income, population, etc. 
    variables = ','.join(['NAME', 'B19013_001E', 'B01003_001E'])

    params = {
        'get': variables,   
        'for': geo['for'],
        'in': geo['in'],
        'key': CENSUS_API_KEY
    }

    resp = requests.get(url, params=params)
    data = resp.json()

    # Seperating paremeter names from data of tract. 
    parameters, values = data[0], data[1]
    result = dict(zip(parameters, values))

    return result


def acsCallWithTiger(lat, lon, radiusMiles):

    # Grab all tracts inside the radius of the specified point. 
    targetTracts = tigerTractQuery(lat, lon, radiusMiles)

    # Since we will fetch tract data by county to minimize calls, gather all unique state + county pairs found in the tracts in the radius 
    # of the location, and pull data for those counties. 
    statesCounties = {(tract['state'], tract['county']) for tract in targetTracts}
        
    
    url = 'https://api.census.gov/data/2023/acs/acs5'

    variables = ','.join(['NAME', 'B19013_001E', 'B01003_001E'])

    allTracts = {}

    for stateCounty in statesCounties: 

        # Retrieving all tract data from a county to minimize API calls. 
        params = {
            'get': variables,   
            'for': f'tract:*',
            'in': f'state:{stateCounty[0]}+county:{stateCounty[1]}', 
            'key': CENSUS_API_KEY
        }

        resp = requests.get(url, params=params)
        response = resp.json()
        # Separating parameter names from data of multiple tracts. 
        parameters, values = response[0], response[1:]

        # Creating object for each tract, and inserting it in dictionary to achieve O(1) lookup time using tract ID. 
        
        for value in values: 
            info = dict(zip(parameters, value))
            geoid = stateCounty[0] + stateCounty[1] + info['tract']
            allTracts[geoid] = info

    # Finally, for each tract that was found within the radius of the specified location using the Census TIGERweb ArcGIS REST service, 
    # Look it up allTracts, where ACS data is available for every tract in the county.
    res = [allTracts.get(tract['geoid'], None) for tract in targetTracts]

    return res

print('break')
print(acsCallWithTiger(43.0387, -76.1337, 1))
print('break')

#  "lat": 43.049345, "lng": -76.138055

[{'NAME': 'Census Tract 43.01; Onondaga County; New York', 'B19013_001E': '13893', 'B01003_001E': '1841', 'state': '36', 'county': '067', 'tract': '004301'}, 
 {'NAME': 'Census Tract 43.02; Onondaga County; New York', 'B19013_001E': '18241', 'B01003_001E': '7628', 'state': '36', 'county': '067', 'tract': '004302'}]

[{'NAME': 'Census Tract 16; Onondaga County; New York', 'B19013_001E': '29974', 'B01003_001E': '3388', 'state': '36', 'county': '067', 'tract': '001600'}, 
 {'NAME': 'Census Tract 23; Onondaga County; New York', 'B19013_001E': '23606', 'B01003_001E': '1701', 'state': '36', 'county': '067', 'tract': '002300'}, 
 {'NAME': 'Census Tract 24; Onondaga County; New York', 'B19013_001E': '58382', 'B01003_001E': '2256', 'state': '36', 'county': '067', 'tract': '002400'}, 
 {'NAME': 'Census Tract 34; Onondaga County; New York', 'B19013_001E': '22358', 'B01003_001E': '1775', 'state': '36', 'county': '067', 'tract': '003400'}]

