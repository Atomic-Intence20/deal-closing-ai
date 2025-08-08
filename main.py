import streamlit as st
import os
from dotenv import load_dotenv
import dashboard
import agents
import tools

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="Deal Closing AI",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar navigation
st.sidebar.title("🚀 Deal Closing AI")
menu = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "📊 Dashboard", "🤖 Agents", "🛠 Tools", "⚙ Settings"]
)

# HOME PAGE
if menu == "🏠 Home":
    st.title("Welcome to Deal Closing AI")
    st.write("""
    This is your AI-powered assistant for automating deal workflows.
    Use the sidebar to explore agents, tools, and the live dashboard.
    """)

# DASHBOARD PAGE
elif menu == "📊 Dashboard":
    st.title("📊 AI Dashboard")
    st.write("Here’s the latest analytics and summaries:")
    dashboard.show_dashboard()  # Ensure dashboard.py has this function

# AGENTS PAGE
elif menu == "🤖 Agents":
    st.title("🤖 AI Agents")
    st.write("Run automated agents for lead analysis, follow-up, and closing.")
    agents.show_agents()  # Ensure agents.py has this function

# TOOLS PAGE
elif menu == "🛠 Tools":
    st.title("🛠 Available Tools")
    tool_list = tools.get_all_tools()  # Ensure tools.py has this function

    selected_tool = st.selectbox("Select a tool", tool_list)
    if st.button("Run Tool"):
        result = tools.run_tool(selected_tool)
        st.success(f"Tool '{selected_tool}' result:")
        st.write(result)

# SETTINGS PAGE
elif menu == "⚙ Settings":
    st.title("⚙ App Settings")
    api_key = st.text_input("Enter API Key", type="password")
    if st.button("Save"):
        os.environ["API_KEY"] = api_key
        st.success("API key saved for session.")
