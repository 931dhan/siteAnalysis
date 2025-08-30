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
        "spatialRel": "esriSpatialRelContains",
        "outFields": "STATE,COUNTY,TRACT,GEOID,NAME",
        "returnGeometry": "false",
        "f": "pjson"
    }
    
    tracts = requests.get(url, params=params).json().get("features", [])    

    # Format each tract in the response into python objects.
    tractInfo = [
        {
            "state": tract["attributes"]["STATE"],
            "county": tract["attributes"]["COUNTY"],
            "tract": tract["attributes"]["TRACT"],
            "geoid": tract["attributes"]["GEOID"],
            "name": tract["attributes"]["NAME"],
        }
        for tract in tracts
    ]

    # Returns a list of tract objects 
    return tractInfo
