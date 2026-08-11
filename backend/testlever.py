from playwright.sync_api import sync_playwright
from adapters.lever import LeverAdapter
import json
from dataclasses import asdict


url = "https://jobs.lever.co/gohighlevel/3f9fe900-c62d-4ea6-9712-ad184a3ff7e1"


with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto(url)

    page.wait_for_load_state("domcontentloaded")

    adapter = LeverAdapter()

    job = adapter.extract_job(page)

    print(json.dumps(asdict(job), indent=4))

    browser.close()