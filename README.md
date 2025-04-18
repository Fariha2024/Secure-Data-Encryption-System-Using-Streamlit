# 🔒 Secure Data Encryption System

A Streamlit-based application for encrypting, storing, and retrieving sensitive data securely.


- 🔑 **User Authentication**
  - Session timeout & reauthorization
  - Lockout after multiple failed attempts

- 🛡️ **Data Encryption**
  - Dual encryption: **Fernet** and **Caesar Cipher**
  - Toggle between encryption types

- 🗃️ **Secure Storage**
  - Data saved with timestamp
  - Stored in local JSON format

- 👁️ **Preview Before Saving**
  - Users can preview encrypted data before confirming storage

- 📜 **Input Validation**
  - Custom validation module to ensure data integrity

- ❗ **Error Logging**
  - Centralized error logging to `error_log.txt`

- 🎨 **Modern UI**
  - Styled with custom CSS for a clean and branded experience



## 🚀 Features
- 🔑 User authentication with session timeout and reauthorization
- 🛡️ Encryption using Fernet and Caesar Cipher
- 🗃️ Secure data storage with timestamp
- 👁️ Encrypted data preview before saving
- 🎨 Modern UI with custom CSS
- 📜 Error logging and input validation

## 📁 Project Structure
SecureDataEncryptionSystem/
├── core/
│   ├── _init_.py             # Empty file
│   ├── storage.py             # Updated for timestamps (Section 11)
│   ├── encryption.py          # Updated for Caesar cipher (Section 12)
│   ├── security.py            # Updated for session timeout (Section 13)
│   └── validation.py          # New file for input validation (Section 10)
├── ui/
│   ├── _init_.py             # Empty file
│   ├── home.py                # Updated for styling (Section 15)
│   ├── store_data.py          # Updated for validation, feedback, cipher toggle, styling
│   ├── retrieve_data.py       # Updated for validation, feedback, cipher toggle, styling
│   ├── login.py               # Updated for styling
│   └── user_auth.py           # Updated for styling
├── data/
│   ├── encrypted_data.json    # Unchanged (JSON storage)
│   └── error_log.txt          # New file for error logging (Section 14)
├── styles/
│   └── custom.css             # New file for CSS styling (Section 15)
├── main.py                    # Updated to initialize new features and styling
└── README.md                  # Optional documentation


## 🛠️ Requirements
- Python 3.9+
- Streamlit
- cryptography

## 📦 Setup Instructions
```bash
pip install -r requirements.txt
streamlit run main.py


🧪 Coming Soon
Multi-user support with hashed passwords

Export encrypted data

Admin dashboard for monitoring sessions


✅ Folder Structure Overview (Developer Notes)
core/ – Backend Logic
storage.py → Handles secure storage + timestamping

encryption.py → Supports Fernet & Caesar Cipher

security.py → Manages session timeout, re-auth, and lockouts

validation.py → Clean input validation layer

__init__.py → Required for module initialization

ui/ – Frontend Pages
Each page (home, login, store/retrieve) in a separate file

Custom CSS from styles/ for professional styling

data/ – Persistent Data
encrypted_data.json → Stores encrypted entries

error_log.txt → Central log for debugging

styles/ – Styling
custom.css → App-wide design and theme control

main.py
Orchestrates the app

Controls session state, page navigation, and reauthorization