# File: SecureDataEncryptionSystem/main.py
import os
import streamlit as st
import time
from ui.home import show_home_page
from ui.store_data import show_store_data_page
from ui.retrieve_data import show_retrieve_data_page
from ui.login import show_login_page
from ui.user_auth import show_user_auth_page
from core.storage import load_data
from core.security import (
    init_session_state, check_reauthorization_required,
    is_locked_out, is_session_expired
)

# Set app title and favicon
st.set_page_config(page_title="Secure Data Encryption System", page_icon="🔒")

# 🔐 Initialize session variables (IMPORTANT)
init_session_state()

# 🔐 Early protection checks
if is_locked_out():
    remaining = int(st.session_state.lockout_time - time.time())
    st.error(f"⛔ Too many failed attempts. Try again in {remaining} seconds.")
    st.session_state.page = "Login"
    st.stop()

if is_session_expired():
    st.error("⏱️ Session expired due to inactivity.")
    st.session_state.authenticated = False
    st.session_state.page = "User Auth"
    st.stop()

# Set default page
if 'page' not in st.session_state:
    st.session_state.page = "User Auth"

def main():
    # Absolute path to custom.css
    css_file_path = r"C:\Users\muham\Documents\assignment5\SecureDataEncryptionSystem\styles\custom.css"
    
    if os.path.exists(css_file_path):
        with open(css_file_path) as f:
            st.markdown(f"<style>{css_file_path}</style>", unsafe_allow_html=True)
    else:
        st.error(f"CSS file not found: {css_file_path}")
    
    st.title("🔒 Secure Data Encryption System")
    load_data()

    menu = ["User Auth", "Home", "Store Data", "Retrieve Data", "Login"]
    choice = st.sidebar.selectbox("Navigation", menu, index=menu.index(st.session_state.page))
    st.session_state.page = choice

    # 🔐 Navigation-level access control (FIXED)
    if 'current_user' not in st.session_state or not st.session_state.authenticated:
        if st.session_state.page not in ["User Auth", "Login"]:
            st.warning("🔒 Please authenticate first.")
            st.session_state.page = "User Auth"
            st.rerun()

    # Render selected page
    if st.session_state.page == "User Auth":
        show_user_auth_page()
    elif st.session_state.page == "Home":
        show_home_page()
    elif st.session_state.page == "Store Data":
        show_store_data_page()
    elif st.session_state.page == "Retrieve Data":
        show_retrieve_data_page()
    elif st.session_state.page == "Login":
        show_login_page()

    # 🔁 Auto-redirect if reauthorization is required mid-session
    if check_reauthorization_required() and st.session_state.page != "Login":
        st.session_state.page = "Login"
        st.rerun()

if __name__ == "__main__":
    main()
