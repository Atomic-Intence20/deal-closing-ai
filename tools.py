# tools.py
# Utility functions for scraping, cleaning, emailing
import requests

def scrape_website(url):
    response = requests.get(url)
    return response.text

def clean_text(text):
    return ' '.join(text.split())