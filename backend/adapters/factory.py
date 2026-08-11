from adapters.greenhouse import GreenhouseAdapter


def get_adapter(url):

    if "greenhouse.io" in url:
        return GreenhouseAdapter()

    raise ValueError(f"Unsupported job site: {url}")