from sys import argv
import math
import uuid
import random as rn
import matplotlib.pyplot as plt

from agent import Agent
from Locations.home import Home
from Locations.office import Office
from simulator import Simulator
from collections import defaultdict

RUN_FROM_TERMINAL = False

"""
Script to initialize the simulation
Example code to run a simulation:
# python3  main.py <Contact tracing en> <#Agents> <#infected> <office_capacity> <mortality_rate> <# days sick> <# days in isolation> <# days simulated> <infecetion risk home> <infection risk work>
# python3 main.py True 1000 20 30 0.05 21 14 30 0.01 0.036
"""
if RUN_FROM_TERMINAL:
	enable_contact_tracing = bool(argv[1])									# Enable contact tracing
	total_agents = int(argv[2])  											# Number of Agents
	initially_infected_agents = int(argv[3])  								# Number of initially infected agents
	initially_healthy_agents = total_agents - initially_infected_agents		# Number of initially healthy agents
	office_capacity = int(argv[4])  										# Capacity of agents per office
	mortality_rate = float(argv[5])  										# Mortality rate
	total_days_sick = int(argv[6])  										# Number of days sick
	days_until_symptoms = int(argv[7])  									# Number of days until symptoms
	total_days_simulated = int(argv[8])  									# Number of days of simulation
	risk_infection_home = float(argv[9])  									# Risk of infection at home
	risk_infection_work = float(argv[10])  									# Risk of infection at work

else:  # ToDo: Put this in a YAML-file
	enable_contact_tracing = False											# Enable contact tracing
	total_agents = 10000                              						# Number of Agents
	initially_infected_agents = 20  										# Number of initially infected agents
	initially_healthy_agents = total_agents - initially_infected_agents  	# Number of initially healthy agents
	office_capacity = 30  													# Capacity of agents per office
	mortality_rate = 0.05  													# Mortality rate
	total_days_sick = 14  													# Number of days sick
	days_until_symptoms = 7  												# Number of days isolation
	total_days_simulated = 14  												# Number of days of simulation
	risk_infection_home = 0.02  												# Risk of infection at home
	risk_infection_work = 0.02  											# Risk of infection at work

# Initialize agents
agent_array = []

print("-- Creating healthy agents --")
for i in range(initially_healthy_agents):
	id = uuid.uuid4().hex
	agent = Agent(id, False, days_until_symptoms, total_days_sick, mortality_rate)
	agent_array.append(agent)

print("-- Creating infected agents --")
for i in range(initially_healthy_agents, total_agents):
	id = uuid.uuid4().hex
	agent = Agent(id, True, days_until_symptoms, total_days_sick, mortality_rate)
	agent_array.append(agent)

# Shuffle the list to mix infected and healthy agents
rn.shuffle(agent_array)


# Create locations
# TODO: We start with households of size 5 and offices of size 30, but this should be improved later
locations = {}
house_capacity = 5  # TODO: Replace with input
number_of_homes = math.ceil(total_agents / house_capacity)

number_of_offices = math.ceil(total_agents / office_capacity)
locations["Homes"] = [Home(house_capacity, risk_infection_home) for _ in range(number_of_homes)]
locations["Offices"] = [Office(office_capacity, risk_infection_work) for _ in range(number_of_offices)]

print("-- Assign agents to households --")
home_index = 0
current_home = locations["Homes"][home_index]
for agent in agent_array:
	if current_home.full_capacity():
		home_index += 1
		current_home = locations["Homes"][home_index]

	current_home.add_agent(agent)
	agent.set_home(current_home)

# Shuffle again to mix households
rn.shuffle(agent_array)

print("-- Assign agents to offices --")
office_index = 0
current_office = locations["Offices"][office_index]
for agent in agent_array:
	if current_office.full_capacity():
		office_index += 1
		current_office = locations["Offices"][office_index]

	current_office.add_agent(agent)
	agent.set_office(current_office)

simulator = Simulator(enable_contact_tracing, locations, agent_array)

while simulator.current_day <= total_days_simulated:
	simulator.step()