from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, String

from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from dotenv import load_dotenv
import os


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Create engine that holds creates and holds onto connections. 
engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True, pool_size=5, future=True)
# Create configuration for sessions. 
Session = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

class Base(DeclarativeBase):
    pass

class AnalyzeQueries(Base): 
    __tablename__ = "analyzequeries"
    
    # Columns 
    id: Mapped[int]
    address: Mapped[str]
    city: Mapped[str]
    state: Mapped[str]
    zipCode: Mapped[str]
    business_type: Mapped[str]
    radius: Mapped[str]
    lat: Mapped[float]
    lon: Mapped[float]
    population: Mapped[int]
    medianincome: Mapped[float]

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, address={self.address!r})"
