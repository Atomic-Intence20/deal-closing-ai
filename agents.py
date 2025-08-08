# agents.py
# Lightweight placeholders for agents (no external LLM required)
# If you later want to add CrewAI, replace these with real Agent code.

def lead_scraper_example(url):
    """Simple example scraper wrapper. Returns scraped text or empty string."""
    from tools import scrape_website, clean_text
    try:
        raw = scrape_website(url)
        return clean_text(raw)
    except Exception:
        return ""

def pitch_writer_example(lead_text):
    """Create a simple pitch text given lead text (placeholder)."""
    return f"Hello — we saw your website and can help. Summary: {lead_text[:300]}"
