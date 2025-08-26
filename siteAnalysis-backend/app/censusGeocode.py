import requests 
import json


def censusGeocode(address: str):

    # We want the geocoding response along with the geographic lookup information for various levels of geography.
    returntype = 'geographies'
    # Inputted location will be formatted as an address in one line. 
    searchtype = 'onelineaddress'

    # Base url for API call. 
    url = f'https://geocoding.geo.census.gov/geocoder/{returntype}/{searchtype}'

    params = {
        'address' : address, 
        'benchmark' : 'Public_AR_Current',
        'vintage' : 'Current_Current',
        'format' : 'json'
    }



    resp = requests.get(url, params=params)
    data = resp.json()['result']['addressMatches'][0]['geographies']['Census Tracts'][0]


    censusLoc = {
        'TRACT':  data['TRACT'],
        'for':  f'tract:{data['TRACT']}',
        'STATE': data['STATE'], 
        'COUNTY': data['COUNTY'],
        'in' :f'state:{data['STATE']}+county:{data['COUNTY']}'
        }
    print(censusLoc)
    return censusLoc

# censusGeocode('111 Small Road, Syracuse NY 13210')