import math
import uuid
import random as rn

from Locations.home import Home
from Locations.office import Office
from agent import Agent
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select

host = "sim-database.cum3wdeshheg.eu-west-2.rds.amazonaws.com"
username = ""
password = ""
port = 3306
dbname = "simdatabase"
engine = create_engine("mysql+pymysql://" + username +":" + password +"@"+host + "/"+dbname,echo = True)
meta = MetaData(engine)
Session = sessionmaker(bind = engine)
session = Session()
conn = engine.connect()

def createhealthyAgent(nr, days_until_symptoms,mortality_rate):
	for i in range(nr):
		id = str(uuid.uuid4().hex)
		session.add(Agent(id = id,is_alive = True,has_symptoms = False, is_isolated = False,
		is_infected= False, has_been_infected = False, days_until_symptoms= days_until_symptoms,
		total_days_sick = 0, total_days_isolated=0, mortality_rate= mortality_rate))
		session.commit()
	return '1'

def createinfectedAgent(nr, days_until_symptoms,mortality_rate):
	for i in range(nr):
		id = str(uuid.uuid4().hex)
		session.add(Agent(id = id,is_alive = True,has_symptoms = False, is_isolated = False,
		is_infected= True, has_been_infected = True, days_until_symptoms= days_until_symptoms,
		total_days_sick = 0,total_days_isolated=0,day_infected=0, mortality_rate= mortality_rate))
		session.commit()
		print("created  infected agent")
	return '1'

def assigntoHousehold(house_id,house_capacity, risk_infection_home, ids):
	table = Table('Agent_Table', meta, autoload=True, autoload_with=engine)
	for i in ids:
		update = table.update().where(table.c.nr==i).values(home=house_id)
		conn.execute(update)
	session.add(Home(capacity=house_capacity, infection_risk=risk_infection_home))
	session.commit()
	return '1'

def assigntoOffice(office_id, office_capacity, risk_infection_work, ids):
	table = Table('Agent_Table', meta, autoload=True, autoload_with=engine)
	for i in ids:
		update = table.update().where(table.c.nr==i).values(office=office_id)
		conn.execute(update)
	session.add(Office(capacity=office_capacity, infection_risk=risk_infection_work))
	session.commit()
	return '1'