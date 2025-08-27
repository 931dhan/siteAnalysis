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

    tracts = requests.get(url, params=params).json().get("features", [])
    
    features = tracts.json()
    # Normalize into a handy list of FIPS tuples and GEOIDs
    
    rows = [
        {
            "state": f["attributes"]["STATE"],
            "county": f["attributes"]["COUNTY"],
            "tract": f["attributes"]["TRACT"],
            "geoid": f["attributes"]["GEOID"],
            "name": f["attributes"]["NAME"],
        }
        for f in features
    ]

    return rows


res = tigerTractQuery(43.0387, -76.1337, 1)

print(res)


# https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/Tracts_Blocks/MapServer/7/query?
# where=&
# text=&
# objectIds=&
# time=&
# timeRelation=esriTimeRelationOverlaps&
# geometry=43.0387%2C+76.1337&
# geometryType=esriGeometryPoint&
# inSR=4326&
# spatialRel=esriSpatialRelIntersects&
# distance=1609.344&
# units=esriSRUnit_Meter&
# relationParam=&
# outFields=STATE%2CCOUNTY%2CTRACT%2CGEOID%2CNAME&
# returnGeometry=false&
# returnTrueCurves=false&
# maxAllowableOffset=&
# geometryPrecision=&
# outSR=&
# havingClause=&
# returnIdsOnly=false&
# returnCountOnly=false&
# orderByFields=&
# groupByFieldsForStatistics=&
# outStatistics=&
# returnZ=false&
# returnM=false&
# gdbVersion=&
# historicMoment=&
# returnDistinctValues=false&
# resultOffset=&
# resultRecordCount=&
# returnExtentOnly=false&
# sqlFormat=none&
# datumTransformation=&
# parameterValues=&
# rangeValues=&
# quantizationParameters=&
# featureEncoding=esriDefault&
# f=pjson

# https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/Tracts_Blocks/MapServer/7/query?
# geometry=%7B%22x%22%3A+-73.9857%2C+%22y%22%3A+40.7484%7D&
# geometryType=esriGeometryPoint&
# inSR=4326&distance=1609.344&
# units=esriSRUnit_Meter&
# spatialRel=esriSpatialRelIntersects&
# outFields=STATE%2CCOUNTY%2CTRACT%2CGEOID%2CNAME&
# returnGeometry=false&
# f=json