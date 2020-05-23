from Locations.location import Location

class Office(Location):
    def __init__(self, i, capacity, infection_risk):
        self.id = f"Office_{i}"
        super().__init__(capacity, infection_risk)