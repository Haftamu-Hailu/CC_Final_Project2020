from Locations.location import Location

class Home(Location):
    def __init__(self, i, capacity, infection_risk):
        self.id = f"Home_{i}"
        super().__init__(capacity, infection_risk)