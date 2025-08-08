import streamlit as st
import random

def show_agents():
    st.subheader("🤖 AI Agents for Deal Closing")

    agent = st.selectbox(
        "Select an agent to run:",
        ["Lead Analysis", "Follow-up Generator", "Deal Closing Assistant"]
    )

    if st.button("Run Agent"):
        if agent == "Lead Analysis":
            st.write("Analyzing leads... 📈")
            st.success("Top leads identified with **78% closing probability**.")
        elif agent == "Follow-up Generator":
            st.write("Generating follow-up email... 📧")
            email = "Hi John, just following up on our last discussion. Looking forward to hearing from you!"
            st.code(email, language="markdown")
        elif agent == "Deal Closing Assistant":
            st.write("Providing deal-closing suggestions... 💼")
            suggestions = [
                "Offer a 5% discount for early sign-up",
                "Highlight limited-time bonus",
                "Send personalized thank-you email"
            ]
            st.write(suggestions[random.randint(0, len(suggestions)-1)])
