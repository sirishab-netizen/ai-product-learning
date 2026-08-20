import json
from pathlib import Path
import sys

# Prefer package import, but fall back to local module when run as a script.
try:
    from learning.week1.day3.policy_checker import check_policy
except Exception:
    try:
        from policy_checker import check_policy
    except Exception:
        check_policy = None

# Default booking used if booking.json is missing.
booking = {
    "traveler": "John",
    "company": "Microsoft",
    "hotel": "Hilton",
    "city": "London",
    "nights": 4,
    "cost": 1860,
}

# Open booking.json relative to this script's directory so the script
# works regardless of the current working directory.
data_path = Path(__file__).resolve().parent / "booking.json"
if data_path.exists():
    with data_path.open() as file:
        booking = json.load(file)

if callable(check_policy):
    result = check_policy(booking)
    print(result)
else:
    print({"approved": None, "reason": "check_policy not available"})