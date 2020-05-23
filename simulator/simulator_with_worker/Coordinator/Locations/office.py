from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
Base = declarative_base()

class Office(Base):
	__tablename__ = 'Office'
	id = Column (Integer, primary_key=True)
	capacity = Column(Integer)
	infection_risk = Column(Float)
	def createOfficeTable(engine):
		Base.metadata.create_all(engine)