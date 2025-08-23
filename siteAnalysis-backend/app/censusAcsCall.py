import requests
import os 
from dotenv import load_dotenv


load_dotenv()
CENSUS_API_KEY = os.getenv("CENSUS_API_KEY")

url = "https://api.census.gov/data/2023/acs/acs5"

# api.census.gov/data/2023/acs/acs5?get=NAME,group(B01001)&for=us:1&key=YOUR_KEY_GOES_HERE
# https://api.census.gov/data/2023/acs/acs5?get=NAME,B01001_001E&for=metropolitan%20division:*&in=metropolitan%20statistical%20area/micropolitan%20statistical%20area:35620
variables = ",".join(["NAME", "B19013_001E", "B01003_001E"])

params = {
    "get": variables,   
    "for": "tract:005602",
    "in": "state:36+county:067",
    "key": CENSUS_API_KEY
}

# resp = requests.Request('GET', url, params=params)
# link  = resp.prepare()
# print(link.url) 

resp = requests.get(url, params=params)
data = resp.json()

headers, values = data[0], data[1]
result = dict(zip(headers, values))

print(result)
