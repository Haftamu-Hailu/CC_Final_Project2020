class Location:
    def __init__(self, capacity, infection_risk):
        self.capacity = capacity
        self.infection_risk = infection_risk
        self.agents = []

    def add_agent(self, agent):
        if len(self.agents) < self.capacity and agent not in self.agents:
            self.agents.append(agent)

    def remove_agent(self, agent):
        if agent in self.agents:
            self.agents.remove(agent)

    def full_capacity(self):
        return len(self.agents) >= self.capacity

    def get_agents(self):
        return self.agents

    def get_infection_risk(self):
        return self.infection_risk

    def isolate_agents(self, current_day):
        for agent in self.agents:
            agent.set_in_isolation(current_day)

