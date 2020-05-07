import random as rn
from saver import Saver

class Simulator:
    def __init__(self, enable_contact_tracing, locations, agent_array):
        self.enable_contact_tracing = enable_contact_tracing
        self.locations = locations
        self.current_day = 0
        self.step_size = 1
        self.agent_array = agent_array

    # Amount of time per step
    def step(self):
        # Simulate infections in each location
        ## TODO: If we want more specific behavior from agents, they should move between the locations
        for location_type in self.locations:  # TODO: This is a place for paralellization
            locations = self.locations[location_type]
            for location in locations:
                simulate_infections(location, self.current_day)

        # Update the status of each agent
        for agent in self.agent_array:  # TODO: This is a place for paralellization
            agent.update_status(self.current_day)

        # With contact tracing, isolate everyone at the locations an agent with symptoms belongs to
        if self.enable_contact_tracing:
            for agent in self.agent_array:
                if agent.has_symptoms:
                    agent.home.isolate_agents(self.current_day)
                    agent.office.isolate_agents(self.current_day)

        self.print_status()
        self.current_day += 1

    def print_status(self):
        total_infected_agents = sum(1 if agent.has_been_infected else 0 for agent in self.agent_array)
        currently_infected_agents = sum(1 if agent.is_infected else 0 for agent in self.agent_array)
        currently_symptomatic_agents = sum(1 if agent.has_symptoms else 0 for agent in self.agent_array)
        total_isolated_agents = sum(1 if agent.is_isolated else 0 for agent in self.agent_array)
        dead_agents = sum(1 if not agent.is_alive else 0 for agent in self.agent_array)

        print(f"Day: {self.current_day} "
              f"Currently infected agents: {currently_infected_agents} "
              f"Total agents with symptoms: {currently_symptomatic_agents} "
              f"Total agents that has been infected: {total_infected_agents} "
              f"Total isolated agents: {total_isolated_agents} "
              f"Total dead agents: {dead_agents}")


def simulate_infections(location, current_day):
    not_isolated = lambda agent: not agent.is_isolated
    is_infected = lambda agent: agent.is_infected
    can_get_infected = lambda agent: not agent.is_infected and not agent.has_been_infected

    agents = list(filter(not_isolated, location.get_agents()))
    infected_agents = list(filter(is_infected, agents))
    healthy_agents = list(filter(can_get_infected, agents))
    for agent in infected_agents:
        for other_agent in healthy_agents:
            if other_agent.can_get_infected():
                infected = gets_infected(location)
                if infected:
                    other_agent.set_infected(current_day)


def gets_infected(location):
    return rn.random() < location.get_infection_risk()
