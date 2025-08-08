import streamlit as st
import random

def get_all_tools():
    return ["Email Generator", "Data Cleaner", "CRM Updater"]

def run_tool(tool_name):
    if tool_name == "Email Generator":
        return "Generated email: Hi there, just touching base regarding our last conversation."
    elif tool_name == "Data Cleaner":
        return f"Cleaned {random.randint(50, 200)} records from the dataset."
    elif tool_name == "CRM Updater":
        return "CRM updated successfully with new lead details."
    else:
        return "Tool not recognized."
