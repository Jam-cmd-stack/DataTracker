import os
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/datatracker")

Base = declarative_base()

class DataRecord(Base):
    __tablename__ = 'data_records'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    value = Column(Float, nullable=False)

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
