from playwright.sync_api import sync_playwright
from dataclasses import dataclass, asdict
import json


@dataclass
class Job:
    title: str
    company: str
    location: str
    description: str
    url: str


with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://job-boards.greenhouse.io/greenhouse/jobs/8052367?gh_jid=8052367")

    page.wait_for_timeout(5000)

    browser.close()