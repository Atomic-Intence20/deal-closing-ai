# main.py
# Orchestrates the agents to run in sequence
from agents import lead_scraper, pitch_writer, follow_up_agent
from tools import scrape_website, clean_text

if __name__ == "__main__":
    url = "https://example.com"
    raw_html = scrape_website(url)
    text = clean_text(raw_html)
    print("Scraped:", text[:200])