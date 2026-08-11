from models import Job
from adapters.base import BaseAdapter


class LeverAdapter(BaseAdapter):

    def extract_job(self, page):

        # Try the og:title meta tag first, then fall back to an empty string.
        title = ""
        try:
            og_title = page.locator("meta[property='og:title']").first.get_attribute("content")
            if og_title:
                title = og_title.strip()
        except Exception:
            title = ""

        company = ""

        location = ""
        location_parts = []

        try:
            loc1 = page.locator("div.sort-by-time.posting-category.medium-category-label.width-full.capitalize-labels.location").first.text_content()
            if loc1:
                location_parts.append(loc1.strip())
        except Exception:
            pass

        try:
            loc2 = page.locator("div.sort-by-time.posting-category.medium-category-label.capitalize-labels.workplaceTypes").first.text_content()
            if loc2:
                location_parts.append(loc2.strip())
        except Exception:
            pass

        location = " ".join(location_parts).strip()

        description = ""
        try:
            desc_block = page.locator("div.section.page-centered[data-qa='job-description']").first
            description_text = desc_block.text_content()
            if description_text:
                description = description_text.strip()
        except Exception:
            pass

        if not description:
            try:
                og_description = page.locator("meta[property='og:description']").first.get_attribute("content")
                if og_description:
                    description = og_description.strip()
            except Exception:
                description = ""

        return Job(
            title=title,
            company=company,
            location=location,
            description=description,
            url=page.url,
            platform="lever"
        )