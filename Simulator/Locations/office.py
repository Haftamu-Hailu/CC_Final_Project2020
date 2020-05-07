from Locations.location import Location

class Office(Location):
    def __init__(self, capacity, infection_risk):
        super().__init__(capacity, infection_risk)