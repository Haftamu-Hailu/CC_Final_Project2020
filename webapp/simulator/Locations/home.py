from simulator.Locations.location import Location

class Home(Location):
    def __init__(self, capacity, infection_risk):
        super().__init__(capacity, infection_risk)