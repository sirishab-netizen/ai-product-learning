from fastapi import FastAPI

from models import Booking, PolicyResult
from policy_engine import evaluate_policy


app = FastAPI()


@app.get("/")
def home():

    return {
        "application": "AI Travel Assistant",
        "version": "0.1.0",
        "status": "running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.post(
    "/policy-check",
    response_model=PolicyResult
)
def policy_check(booking: Booking):

    return evaluate_policy(booking)