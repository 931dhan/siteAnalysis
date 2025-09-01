from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True, pool_size=5, future=True)

Session = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
