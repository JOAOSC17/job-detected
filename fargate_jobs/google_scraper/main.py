import asyncio
import sys
from scraper import scrape_google_links

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py '<search_query>'")
        sys.exit(1)
    
    query = sys.argv[1]
    links = asyncio.run(scrape_google_links(query))
    print("[SCRAPED LINKS]")
    for link in links:
        print(link)