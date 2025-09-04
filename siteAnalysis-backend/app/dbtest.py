from sqlalchemy.orm import sessionmaker
from models import AnalyzeQueries, Session
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, String

from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from dotenv import load_dotenv
import os

with Session() as session: 
    syracuse = AnalyzeQueries(
        id="2",
        address = "300 S Crouse Ave, Syracuse, NY 13210",
        city = "Syracuse", 
        state = "NY", 
        zipCode = "13210", 
        business_type = "Cafe", 
        radius = "1", 
        lat = 43.0402379, 
        lon = -76.13695,
        population = 11244,
        medianincome = 18179.012006403416) 
    
    session.add(syracuse)
    session.commit()