# This module prefers absolute package imports. If run as a script
# (e.g. `python learning/week1/day2/main.py`) the package root may not
# be on `sys.path`. Try the absolute imports first and fall back to
# inserting the workspace root into `sys.path` if needed.
from learning.week1.day2 import booking


try:
    from learning.week1.day2.hotel import Hotel
    from learning.week1.day2.traveler import Traveler
    from learning.week1.day2.booking import Booking
except ModuleNotFoundError:
    from pathlib import Path
    import sys

    workspace_root = Path(__file__).resolve().parents[3]
    if str(workspace_root) not in sys.path:
        sys.path.insert(0, str(workspace_root))

    from learning.week1.day2.hotel import Hotel
    from learning.week1.day2.traveler import Traveler
    from learning.week1.day2.booking import Booking


def main() -> None:
    print("Welcome to AI Travel Assistant")

    john = Traveler(
        "John",
        "Microsoft"
    )

    hilton = Hotel(
        "Hilton",
        "London",
        240,
        5
    )

    print(hilton.name)
    print(hilton.city)
    print(hilton.total_cost(4))
    print(hilton.summary())

    booking = Booking(
      john,
      hilton,
      4,
      900
    )

    print(booking.nights)

    print(
        booking.total_trip_cost()
    )

    print(
        booking.is_policy_compliant()
    )

    print(
    booking.summary()
    )

if __name__ == "__main__":
    main()
#mary = Traveler(
#    "Mary",
#    "Google"
#)