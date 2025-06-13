import streamlit as st

# App Title
st.set_page_config(page_title="Amber – AI Agency Assistant", layout="centered")
st.title("🤖 Meet Amber – Your AI Agency Assistant")

# Agent Description
st.markdown("""
Amber is designed to make your experience smooth and efficient.  
She can:
- Answer questions about our packages and pricing
- Recommend the best solution for your business
- Schedule discovery calls
- Send follow-up emails
- Generate invoices and collect payments
- Handle onboarding for new clients
""")

st.divider()

# Simulated options
st.subheader("How can Amber help you today?")

option = st.selectbox("Choose a task:", [
    "Learn about packages & pricing",
    "Get a recommendation",
    "Schedule a call",
    "Request an invoice",
    "Make a payment",
    "Start onboarding",
    "Ask a custom question"
])

# Simulated responses
if option == "Learn about packages & pricing":
    st.info("Amber: We offer flexible packages based on your business size and needs. Would you like to view our package list?")
elif option == "Get a recommendation":
    st.info("Amber: Let’s find the best solution for your business. Please tell me a bit about your company’s needs.")
elif option == "Schedule a call":
    st.info("Amber: You can book a discovery call using our calendar. [Link Placeholder]")
elif option == "Request an invoice":
    st.info("Amber: Please provide your email and package selection, and I’ll send your invoice shortly.")
elif option == "Make a payment":
    st.info("Amber: You can securely pay using our online system. [Payment Link Placeholder]")
elif option == "Start onboarding":
    st.info("Amber: Let’s begin onboarding. I’ll guide you through each step. [Onboarding Form Placeholder]")
elif option == "Ask a custom question":
    user_question = st.text_input("Type your question for Amber:")
    if user_question:
        st.success(f"Amber: Thank you for your question! I'll get back to you shortly with an answer to: '{user_question}'")

