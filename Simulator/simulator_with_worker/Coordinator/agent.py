from sqlalchemy import Table, Column, Integer,Boolean, Float, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Agent(Base):
	__tablename__ = 'Agent_Table'
	nr = Column(Integer, primary_key=True)
	id = Column(String(32))
	is_alive = Column(Boolean)
	has_symptoms = Column(Boolean)
	is_isolated = Column(Boolean)
	is_infected = Column(Boolean)
	has_been_infected = Column(Boolean)

	day_infected = Column(Integer)
	day_isolated = Column(Integer)

	days_until_symptoms = Column(Integer)
	total_days_sick = Column(Integer)
	total_days_isolated = Column(Integer)
	mortality_rate = Column(Float)

	home = Column(Integer)
	office = Column(Integer)
	def createAgentTable(engine):
		Base.metadata.create_all(engine)