def check_policy(booking):

    violations = []

    if booking["cost"] > 2000:
        violations.append("Trip exceeds $2,000 policy limit")

    if booking["travel_category"] == "Hotel" and booking["payment_method"] == "Individual Card":
        violations.append("Individual Card is not allowed for hotel bookings")

    if violations:
        return {
            "approved": False,
            "violations": violations
        }

    return {
        "approved": True,
        "violations": []
    }