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
    response = r.json()
    header, data = response[0], response[1:]

    print(header)
    return ''


acsCall('111 Small Road, Syracuse NY 13210')
acsCallWithTiger('36', '067')

# https://api.census.gov/data/2023/acs/acs5?
# get=NAME%2CB19013_001E%2CB01003_001E&
# for=tract%3A005602&
# in=state%3A36%2Bcounty%3A067&
# key=disabledAPIkey

# http://api.census.gov/data/2023/acs/acs5?
# get=NAME%2CB19013_001E%2CB01003_001E&
# for=tract%3A*&
# in=state%3A36%2Bcounty%3A004200&
# key=disabledAPIkey