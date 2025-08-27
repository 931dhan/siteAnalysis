import requests
import os 
from dotenv import load_dotenv
from censusGeocode import censusGeocode


load_dotenv()
CENSUS_API_KEY = os.getenv('CENSUS_API_KEY')


def acsCall(address): 

    # Base URL for API calls to Census ACS API 
    # Example of a call
    # https://api.census.gov/data/2023/acs/acs5?get=NAME,B01001_001E&for=metropolitan%20division:*&in=metropolitan%20statistical%20area/micropolitan%20statistical%20area:3562
    url = 'https://api.census.gov/data/2023/acs/acs5'

    # Find the tract, state, and county of address. 
    geo = censusGeocode(address)

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

    headers, values = data[0], data[1]
    result = dict(zip(headers, values))

    return result

def acsCallWithTiger(state, county):
    
    url = 'https://api.census.gov/data/2023/acs/acs5'

    variables = ','.join(['NAME', 'B19013_001E', 'B01003_001E'])

    params = {
        'get': variables,   
        'for': f'tract:*',
        'in': f'state:{state}+county:{county}', 
        'key': CENSUS_API_KEY
    }

    r = requests.get(url, params=params)
    rows = r.json()
    header, data = rows[0], rows[1:]

    print(data)

acsCallWithTiger('36', '004200')