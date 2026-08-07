from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://google.com")

    page.locator("[name='q']").fill("Playwright Python")

    page.locator("[name='q']").press("Enter")

    page.screenshot(path="screenshot.png", full_page=True)

    page.wait_for_timeout(5000)

    browser.close()