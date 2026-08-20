from pydantic import BaseModel


class Booking(BaseModel):
    traveler: str
    company: str
    cost_center: str
    billing_entity: str
    cost: float
    travel_category: str
    payment_method: str

class PolicyResult(BaseModel):
    approved: bool
    violations: list[str]