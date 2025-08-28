import requests 
import json

def tigerTractQuery(lat, lon, radiusMiles):

    url = f'https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/Tracts_Blocks/MapServer/7/query'

    params = { 
        "geometry": f"{lon}, {lat}",
        "geometryType" : "esriGeometryPoint", 
        # inSR refers to how we want to interpret the entered location. EPSG:4326 refers to standard GPS lat/lon. 
        "inSR": 4326, 
        "distance": radiusMiles * 1609.344,
        "units": "esriSRUnit_Meter",
        # spatialRel refers to how we want geometry to interact with the radius. 
        "spatialRel": "esriSpatialRelIntersects",
        "outFields": "STATE,COUNTY,TRACT,GEOID,NAME",
        "returnGeometry": "false",
        "f": "pjson"
    }

    response = requests.get(url, params=params).json().get("features", [])
    
    tracts = response
    
    tractInfo = [
        {
            "state": t["attributes"]["STATE"],
            "county": t["attributes"]["COUNTY"],
            "tract": t["attributes"]["TRACT"],
            "geoid": t["attributes"]["GEOID"],
            "name": t["attributes"]["NAME"],
        }
        for t in tracts
    ]

    return tractInfo


res = tigerTractQuery(43.0387, -76.1337, 1)

print(res)

