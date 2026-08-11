from models import Job
from adapters.base import BaseAdapter


class GreenhouseAdapter(BaseAdapter):

    def extract_job(self, page):
        """
        Extract job details from a Greenhouse job page or popup
        """

        # --- Title ---
        title = None
        try:
            title = page.locator("div.job__header h1.section-header, h1.section-header.section-header--large.font-primary").first.text_content()
            if title:
                title = title.strip()
        except Exception:
            title = None
        if not title:
            try:
                title = page.locator("meta[property='og:title']").get_attribute("content")
            except Exception:
                title = "N/A"

        # --- Location ---
        location = None
        try:
            location = page.locator("div.job__location div").first.text_content()
            if location:
                location = location.strip()
        except Exception:
            location = None
        if not location:
            try:
                location = page.locator("meta[property='og:location']").get_attribute("content")
            except Exception:
                location = "N/A"

        # --- Description ---
        description = None
        # Try to get a visible description block first
        try:
            desc_loc = page.locator("div.job__description, div.job-description, div[class*='description'], div#content, .content").first
            description = desc_loc.text_content()
            if description:
                description = description.strip()
        except Exception:
            description = None
        if not description:
            try:
                description = page.locator("meta[property='og:description']").get_attribute("content")
            except Exception:
                description = "N/A"

        # --- Company ---
        company = None
        try:
            company = page.locator(".company-name").first.text_content()
            if company:
                company = company.strip()
        except Exception:
            company = None
        if not company:
            try:
                company = page.locator("meta[property='og:site_name']").get_attribute("content")
            except Exception:
                company = "Unknown"

        # --- URL ---
        url = page.url

        # Return structured object
        return Job(
            title=title,
            company=company,
            location=location,
            description=description,
            url=url,
            platform="greenhouse"
        )