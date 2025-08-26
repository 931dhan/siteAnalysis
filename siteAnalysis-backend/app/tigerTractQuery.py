import requests 
import json

def tigerTractQuery(lat, lon, radiusMiles):

    initialLocation = json.dumps({
        "x": float(lat),
        "y": float(lon)
    })

    url = f'https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/Tracts_Blocks/MapServer/7/query'

    params = { 
        "geometry": initialLocation,
        "geometryType" : "esriGeometryPoint", 
        # inSR refers to how we want to interpret the entered location. EPSG:4326 refers to standard GPS lat/lon. 
        "inSR": 4326, 
        "distance": radiusMiles * 1609.344,
        "units": "esriSRUnit_Meter",
        # spatialRel refers to how we want geometry to interact with the radius. 
        "spatialRel": "esriSpatialRelInteresects",
        "outFields": "STATE,COUNTY,TRACT,GEOID,NAME",
        "returnGeometry": "false",
        "f": "json"
    }
    
    tracts = requests.get(url, params=params, timeout=30)

    return tracts


res = tigerTractQuery(-73.9857, 40.7484, 1)

print(res)