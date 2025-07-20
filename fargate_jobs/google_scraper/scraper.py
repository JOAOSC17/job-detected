from apify_client import ApifyClient
from dotenv import load_dotenv
import os

load_dotenv()
api_apify_key = os.getenv("APIFY_KEY")
actor_id = os.getenv("ACTOR_ID")
async def scrape_google_links(query):
    print(api_apify_key)
    if not api_apify_key:
        raise ValueError("APIFY_KEY not found in environment variables. Please check your .env file.")
    
    client = ApifyClient(api_apify_key)

    run_input = {
        "queries": query,
        "resultsPerPage": 100,
        "maxPagesPerQuery": 1,
        "focusOnPaidAds": False,
        "searchLanguage": "",
        "languageCode": "",
        "forceExactMatch": False,
        "wordsInTitle": [],
        "wordsInText": [],
        "wordsInUrl": [],
        "mobileResults": False,
        "includeUnfilteredResults": False,
        "saveHtml": False,
        "saveHtmlToKeyValueStore": False,
        "includeIcons": False,
    }

    try:
        run = client.actor(actor_id).call(run_input=run_input)
        links = []
        organic_results = []
        for item in client.dataset(run["defaultDatasetId"]).iterate_items():
            if "organicResults" in item and len(item["organicResults"]) > 0:
                organic_results = item["organicResults"]
        for result in organic_results:
            if "url" in result:
                links.append(result["url"])
        return links
        
    except Exception as e:
        print(f"Error running Apify actor: {e}")
        return []


