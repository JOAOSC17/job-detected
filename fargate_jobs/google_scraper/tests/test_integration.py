import os
import pytest
from scraper import scrape_google_links

@pytest.mark.asyncio
async def test_scrape_google_links(monkeypatch):
    monkeypatch.setenv("APIFY_KEY", os.getenv("APIFY_KEY", "test_fake_key"))
    monkeypatch.setenv("ACTOR_ID", os.getenv("ACTOR_ID", "actor_id"))

    query = "site:https://jobs[.]lever[.]co 'react' 'remote'"
    try:
        results = await scrape_google_links(query)
        assert isinstance(results, list)
        assert all(isinstance(url, str) for url in results)
    except ValueError as e:
        assert "APIFY_KEY not found" in str(e)
