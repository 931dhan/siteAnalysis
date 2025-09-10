from sqlalchemy.orm import sessionmaker
from models import AnalyzeQueries, Session
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, String

from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from dotenv import load_dotenv
import os

# load_dotenv()
# DATABASE_URL = os.getenv("DATABASE_URL")

# # Create engine that holds creates and holds onto connections. 
# engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True, pool_size=5, future=True)
# # Create configuration for sessions. 
# Session = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

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