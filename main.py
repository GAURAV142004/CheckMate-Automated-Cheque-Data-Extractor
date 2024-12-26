import streamlit as st
from authentication import login_signup
from homepage import homepage

# Initialize session state for authentication
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# Check authentication status
if not st.session_state["authenticated"]:
    # Render login/signup functionality
    login_signup()
else:
    # Render homepage functionality
    homepage()
