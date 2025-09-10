from models import AnalyzeQueries, Session
from sqlalchemy import select, and_


def queryAdd(businessInfo): 

    with Session() as session: 
        businessRow = AnalyzeQueries(
            id="3",
            address = businessInfo['address'],
            city = businessInfo['city'], 
            state = businessInfo['state'], 
            zipCode = businessInfo['zipCode'], 
            business_type = businessInfo['business_type'], 
            radius = businessInfo['radius'], 
            lat = businessInfo['lat'], 
            lon = businessInfo['lon'],
            population = businessInfo['population'],
            medianincome = businessInfo['medianincome']) 
        
        session.add(businessRow)
        session.commit()


def querySelect(businessInfo): 
    with Session() as session: 
        
        selectQuery = select(AnalyzeQueries).where(
            and_(
                AnalyzeQueries.id == '1',
                AnalyzeQueries.state == 'NY'
            )
        )
        rows = session.scalars(selectQuery).first()
    
    return rows

print(querySelect({}))  