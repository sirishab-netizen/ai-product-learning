from models import Booking, PolicyResult

def evaluate_policy(booking: Booking) -> PolicyResult:

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

    return PolicyResult(
        approved=len(violations) == 0,
        violations=violations
    )