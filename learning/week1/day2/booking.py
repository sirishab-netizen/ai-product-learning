class Booking:

    def __init__(
        self,
        traveler,
        hotel,
        nights,
        flight_cost
    ):
        self.traveler = traveler
        self.hotel = hotel
        self.nights = nights
        self.flight_cost = flight_cost
    def total_trip_cost(self):
        hotel_cost = self.hotel.total_cost(self.nights)
        return hotel_cost + self.flight_cost

    def is_policy_compliant(self):
        return self.total_trip_cost() <= 2000

    def summary(self):
        return (
            f"{self.traveler.name} from "
            f"{self.traveler.company} is traveling to "
            f"{self.hotel.city} and staying at "
            f"{self.hotel.name} for {self.nights} nights. "
            f"Total trip cost: ${self.total_trip_cost()}."
        )