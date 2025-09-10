import requests 
import json


def censusGeocode(lat, lon):

    # We want the geocoding response along with the geographic lookup information for various levels of geography.
    returntype = 'geographies'
    # Inputted location will be formatted as an address in one line. 
    searchtype = 'coordinates'

    # Base url for API call. 
    url = f'https://geocoding.geo.census.gov/geocoder/{returntype}/{searchtype}'

    params = {
        'x' :  lon,
        'y' : lat,
        'benchmark' : 'Public_AR_Current',
        'vintage' : 'Current_Current',
        'format' : 'json'
    }
    
    

    resp = requests.get(url, params=params)
    data = resp.json()['result']['geographies']['Census Tracts'][0]


    censusLoc = {
        'TRACT':  data['TRACT'],
        'for':  f'tract:{data['TRACT']}',
        'STATE': data['STATE'], 
        'COUNTY': data['COUNTY'],
        'in' :f'state:{data['STATE']}+county:{data['COUNTY']}'
        }

    return censusLoc

# print(censusGeocode('43.0387', '-76.1337'))