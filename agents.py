# agents.py
# Defines AI agents for scraping, pitching, and follow-up

from crewai import Agent

lead_scraper = Agent(name="Lead Scraper", role="Scrapes lead data from sources")
pitch_writer = Agent(name="Pitch Writer", role="Creates personalized sales pitches")
follow_up_agent = Agent(name="Follow Up", role="Sends follow-up emails to warm leads")