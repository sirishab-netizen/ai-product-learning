from adapters.greenhouse import GreenhouseAdapter
from adapters.lever import LeverAdapter


def get_adapter(url):

    if "greenhouse.io" in url:
        return GreenhouseAdapter()

    if "lever.co" in url:
        return LeverAdapter()

    raise ValueError(f"Unsupported job site: {url}")