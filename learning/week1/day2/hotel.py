class Hotel:

    def __init__(self, name, city, nightly_rate, stars):
        self.name = name
        self.city = city
        self.nightly_rate = nightly_rate
        self.stars = stars

    def total_cost(self, nights):
        return self.nightly_rate * nights

    def summary(self):
        return f"{self.name} is a {self.stars}-star hotel in {self.city}."