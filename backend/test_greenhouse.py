from playwright.sync_api import sync_playwright
from adapters.greenhouse import GreenhouseAdapter
import os
import threading
import sys
import json
from dataclasses import asdict

url = "https://job-boards.greenhouse.io/greenhouse/jobs/8052367?gh_jid=8052367"


def run():
    headless = os.getenv("HEADLESS", "0") == "1"
    timeout_seconds = int(os.getenv("TEST_TIMEOUT", "15"))

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        page = browser.new_page()

        # Watchdog: set an abort flag if the test hangs (safer than force-closing)
        abort_event = threading.Event()

        def _signal_abort():
            try:
                print(f"[watchdog] timeout reached ({timeout_seconds}s), signalling abort...", file=sys.stderr)
                abort_event.set()
            except Exception:
                pass

        timer = threading.Timer(timeout_seconds, _signal_abort)
        timer.start()

        try:
            # Use a bounded navigation wait to avoid hanging when pages keep network connections open
            page.goto(url, wait_until="load", timeout=20000)

            # Wait for a stable indicator (title meta or company name) instead of a fixed timeout
            try:
                page.wait_for_selector("meta[property='og:title'], .company-name", timeout=10000)
            except Exception:
                # Fallback to a short timeout so test still progresses
                page.wait_for_timeout(2000)

            # Abort if watchdog signalled before extraction
            if abort_event.is_set():
                raise TimeoutError("Test aborted by watchdog before extraction")

            adapter = GreenhouseAdapter()
            job = adapter.extract_job(page)

            if abort_event.is_set():
                raise TimeoutError("Test aborted by watchdog during/after extraction")

            # Surface the extracted job and perform basic assertions
            #print(job)
            #print(json.dumps(asdict(job), indent=4))
            os.makedirs("jobs", exist_ok=True)
            with open("jobs/greenhouse.json", "w", encoding="utf-8") as f:
                json.dump(asdict(job), f, indent=4)
            assert job is not None
            assert isinstance(job.url, str) and job.url.startswith("http"), "invalid url"
            assert job.title is not None and job.title != "N/A", "missing title"
            assert job.company is not None, "missing company"
            assert job.location is not None, "missing location"
            assert job.description is not None, "missing description"

        finally:
            try:
                timer.cancel()
            except Exception:
                pass
            try:
                browser.close()
            except Exception:
                pass


if __name__ == "__main__":
    run()