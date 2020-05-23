import math
import random as rn

from sqlalchemy import create_engine, or_, and_, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import select

host = "sim-database.cum3wdeshheg.eu-west-2.rds.amazonaws.com"
username = ""
password = ""
port = 3306
dbname = "simdatabase"
engine = create_engine("mysql+pymysql://" + username +":" + password +"@"+host + "/"+dbname,echo = True)
meta = MetaData(engine)
conn = engine.connect()

def gets_infected(risk):
	return rn.random() < risk

def simulate_infection(location, array_subjects, risk, current_day):
	table = Table('Agent_Table', meta, autoload=True, autoload_with=engine)
	#get all agents in office, if one is infected, tfest if more get infected,
	if location == 'office':
		for office in array_subjects:
			select_o= table.select().where(and_(table.c.office == office, table.c.is_isolated == False))
			agents_in_office1 = conn.execute(select_o)

			for agent in agents_in_office1:
				if agent.is_infected:
					select_o= table.select().where(and_(table.c.office == office, table.c.is_isolated == False))
					agents_in_office = conn.execute(select_o)
					for agent2 in agents_in_office:
						i = agent2.nr
						if gets_infected(risk) and not agent2.is_infected:
							print("Agent is infected nr: ", agent2.nr)
							update = table.update().where(table.c.nr==i).values(is_infected=True, has_been_infected=True,day_infected=current_day)
							conn.execute(update)
		return '1'
	elif location == 'home':
		for home in array_subjects:
			select_o= table.select().where(and_(table.c.home == home, table.c.is_isolated == False))
			agents_in_home1 = conn.execute(select_o)
			for agent in agents_in_home1:
				if agent.is_infected:
					select_o= table.select().where(and_(table.c.home == home, table.c.is_isolated == False))
					agents_in_home = conn.execute(select_o)
					for agent2 in agents_in_home:
						i = agent2.nr
						if gets_infected(risk) and not agent.is_infected:
							update = table.update().where(table.c.nr==i).values(is_infected=True, has_been_infected=True,day_infected=current_day)
							conn.execute(update)
		return '1'


def end_of_day(contact_tracing, max_sick_time, current_day):
	table = Table('Agent_Table', meta, autoload=True, autoload_with=engine)
	select_o= table.select().where(and_(or_(table.c.is_infected == True, table.c.is_isolated == True), table.c.is_alive ==True))
	agents = conn.execute(select_o)
	for agent in agents:
		i = agent.nr
		
		if (agent.total_days_sick == agent.days_until_symptoms):
			update2 = table.update().where(table.c.nr==i).values(has_symptoms=True, is_isolated=True)
			conn.execute(update2)
			office = agent.office
			home = agent.home
			#contact_tracing
			table = Table('Agent_Table', meta, autoload=True, autoload_with=engine)
			select_o= table.select().where(or_(table.c.office == office, table.c.home == home))
			contacts = conn.execute(select_o)
			for contact in contacts:
				update = table.update().where(table.c.nr==contact.nr).values(is_isolated=True, day_isolated=current_day)
				conn.execute(update)

			
		if (agent.total_days_sick == max_sick_time):
			if gets_infected(agent.mortality_rate)==True:
				update2 = table.update().where(table.c.nr==i).values(is_alive=False,is_infected = False,has_symptoms = False, is_isolated=True)
			else:
				update2 = table.update().where(table.c.nr==i).values(is_infected=False,has_symptoms=False, is_isolated=False)
			conn.execute(update2)
		if agent.is_infected == True:
			total_days_sick = agent.total_days_sick + 1
			update1 = table.update().where(table.c.nr==i).values(total_days_sick=total_days_sick)
			conn.execute(update1)
			
		if agent.is_isolated == True:
			if agent.total_days_isolated == 10:
				update1 = table.update().where(table.c.nr==i).values(is_isolated=False)
			else:
				total_days_isolated = agent.total_days_isolated + 1
				update1 = table.update().where(table.c.nr==i).values(total_days_isolated=total_days_isolated)
			conn.execute(update1)
	return 'end_of_day'