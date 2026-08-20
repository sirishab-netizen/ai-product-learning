from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Booking(BaseModel):
    traveler: str
    company: str
    cost_center: str
    billing_entity: str
    cost: float
    travel_category: str
    payment_method: str


@app.get("/")
def home():
    return {
        "message": "AI Travel Assistant API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/policy-check")
def policy_check(booking: Booking):

    violations = []

    if booking.cost > 2000:
        violations.append(
            "Trip exceeds $2,000 policy limit"
        )

    if (
        booking.travel_category == "Hotel"
        and booking.payment_method == "Individual Card"
    ):
        violations.append(
            "Individual Card is not allowed for hotel bookings"
        )

    return {
        "approved": len(violations) == 0,
        "violations": violations
    }