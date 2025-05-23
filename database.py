# database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL that connects to your SQL database
#update with username, password, and name
DATABASE_URL = "postgresql://username:password@localhost/medefacts"

# database engine
engine = create_engine(DATABASE_URL) 

# database session
SessionLcal + sessionmaker(autocommit=False, autoflush=False, autoflush=False, bind=engine) 

# base class for tables
Base = declarative_base()
