import streamlit as st
import pandas as pd
import random

def show_dashboard():
    st.subheader("📊 Sales Performance Overview")

    # Fake data for demo
    data = {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "Deals Closed": [random.randint(5, 20) for _ in range(5)],
        "Revenue ($k)": [random.randint(20, 100) for _ in range(5)],
        "Conversion Rate (%)": [round(random.uniform(10, 40), 2) for _ in range(5)]
    }
    df = pd.DataFrame(data)

    st.dataframe(df)

    st.line_chart(df.set_index("Month")[["Deals Closed", "Revenue ($k)"]])
    st.bar_chart(df.set_index("Month")["Conversion Rate (%)"])

    st.success("AI Insight: April saw a **15% jump** in conversion rates due to targeted outreach.")
