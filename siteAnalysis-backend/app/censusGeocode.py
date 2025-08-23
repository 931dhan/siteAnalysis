import requests 
import json

returntype = "geographies"
searchtype = "onelineaddress"

url = f"https://geocoding.geo.census.gov/geocoder/{returntype}/{searchtype}"


params = {
    "address" : "111 Small Rd, Syracuse NY 13210", 
    "benchmark" : "Public_AR_Current",
    "vintage" : "Current_Current",
    "format" : "json"
}



resp = requests.get(url, params=params)
data = resp.json()['result']['addressMatches'][0]['geographies']['Census Tracts'][0]


censusLoc = {
    'TRACT':  data['TRACT'],
    'STATE': data['STATE'], 
    'COUNTY': data['COUNTY']
    }

print(censusLoc)