from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


import os


# engine = create_engine(os.getenv("SQLALCHEMY_DATABASE_URL"))
engine = create_engine("postgresql://114.70.23.79:5432/spring?user=chaeda&password=chaeda")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
