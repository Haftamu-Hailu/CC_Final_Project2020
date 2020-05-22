from sys import argv

from initializer import initialize
from simulator import Simulator
from saver import Saver

RUN_FROM_TERMINAL = False

"""
Script to initialize the simulation
Example code to run a simulation:
# python3  main.py <Contact tracing en> <#Agents> <#infected> <office_capacity> <house_capacity> <mortality_rate> <# days sick> <# days in isolation> <# days simulated> <infecetion risk home> <infection risk work>
# python3 main.py True 1000 20 30 5 0.05 21 14 30 0.01 0.036
"""
if RUN_FROM_TERMINAL:
    enable_contact_tracing = bool(argv[1])  # Enable contact tracing
    total_agents = int(argv[2])  # Number of Agents
    initially_infected_agents = int(argv[3])  # Number of initially infected agents
    initially_healthy_agents = total_agents - initially_infected_agents  # Number of initially healthy agents
    office_capacity = int(argv[4])  # Capacity of agents per office
    house_capacity = int(argv[5])  # Capacity of agents per house
    mortality_rate = float(argv[6])  # Mortality rate
    total_days_sick = int(argv[7])  # Number of days sick
    days_until_symptoms = int(argv[8])  # Number of days until symptoms
    total_days_simulated = int(argv[9])  # Number of days of simulation
    risk_infection_home = float(argv[10])  # Risk of infection at home
    risk_infection_work = float(argv[11])  # Risk of infection at work
    verbose = bool(argv[13])  # If we want printing during simulator run

else:  # ToDo: Put this in a YAML-file
    enable_contact_tracing = False  # Enable contact tracing
    total_agents = 1000  # Number of Agents
    initially_infected_agents = 20  # Number of initially infected agents
    initially_healthy_agents = total_agents - initially_infected_agents  # Number of initially healthy agents
    office_capacity = 30  # Capacity of agents per office
    house_capacity = 5  # Capacity of agents per house
    mortality_rate = 0.05  # Mortality rate
    total_days_sick = 14  # Number of days sick
    days_until_symptoms = 7  # Number of days isolation
    total_days_simulated = 14  # Number of days of simulation
    risk_infection_home = 0.02  # Risk of infection at home
    risk_infection_work = 0.02  # Risk of infection at work
    verbose = True  # If we want printing during simulator run

locations, agent_array = initialize(total_agents, initially_infected_agents, initially_healthy_agents,
                                    office_capacity, house_capacity, mortality_rate, total_days_sick,
                                    days_until_symptoms, total_days_simulated, risk_infection_home, risk_infection_work)

saver = Saver(verbose)
simulator = Simulator(enable_contact_tracing, locations, agent_array, saver)

while simulator.current_day <= total_days_simulated:
    simulator.step()

saver.print_overview()