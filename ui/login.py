# File: SecureDataEncryptionSystem/ui/login.py

import streamlit as st
from core.security import reauthorize, is_locked_out

def show_login_page():
    """
    Display the Login Page for reauthorization after too many failed attempts.
    """
    st.subheader("🔑 Reauthorization Required")

    login_pass = st.text_input("Enter Master Password:", type="password", key="login_pass")

    if st.button("Login"):
        if is_locked_out():
            st.error("❌ Your account is locked due to too many failed attempts. Please try again later.")
        elif reauthorize(login_pass):
            st.success("✅ Reauthorized successfully! Redirecting to Retrieve Data...")
            st.session_state.page = "Retrieve Data"
        else:
            st.error("❌ Incorrect password! Please try again.")
