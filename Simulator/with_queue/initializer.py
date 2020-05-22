import math
import uuid
import random as rn

from agent import Agent
from Locations.home import Home
from Locations.office import Office


def initialize(total_agents, initially_infected_agents, initially_healthy_agents, office_capacity,
               house_capacity, mortality_rate, total_days_sick, days_until_symptoms, total_days_simulated,
               risk_infection_home, risk_infection_work):

    # Create agents
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
    locations = {}
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

    return locations, agent_array
