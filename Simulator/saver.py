from collections import defaultdict
import matplotlib.pyplot as plt
from mysql_database import MySQLDatabase


class Saver:
    def __init__(self, verbose):
        """
        This class is meant as middleman-function - so it is easy to change where we want to store things without changing the simulator
        :param verbose: If we want to print the output
        """
        self.verbose = verbose
        self.db = MySQLDatabase()
        self.overview = defaultdict(lambda: [])
        self.infections = []

    def save_overview(self, day, currently_infected_agents, total_infected_agents, currently_symptomatic_agents, total_isolated_agents, dead_agents):
        self.db.insert_overview_data(day, currently_infected_agents, total_infected_agents, currently_symptomatic_agents, total_isolated_agents, dead_agents)
        if self.verbose:
            print(f"Day: {day} "
                  f"Currently infected agents: {currently_infected_agents} "
                  f"Total agents with symptoms: {currently_symptomatic_agents} "
                  f"Total agents that has been infected: {total_infected_agents} "
                  f"Total isolated agents: {total_isolated_agents} "
                  f"Total dead agents: {dead_agents}")

    def save_infection_data(self, infecter, infected, location, day):
        self.infections.append((infecter, infected, location, day))

    def print_overview(self):
        for key in self.overview:
            plt.plot(self.overview[key])
            plt.title(key)
            plt.show()
