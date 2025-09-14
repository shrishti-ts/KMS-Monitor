# utils/crypto.py
from cryptography.fernet import Fernet
import os

FERNET_KEY = os.environ.get("FERNET_KEY")
if not FERNET_KEY:
    raise ValueError("FERNET_KEY not set in environment")

fernet = Fernet(FERNET_KEY.encode())

def encrypt(text: str) -> bytes:
    """Encrypt the input text using Fernet."""
    return fernet.encrypt(text.encode())

def decrypt(token: bytes) -> str:
    """Decrypt the input token using Fernet."""
    return fernet.decrypt(token).decode()
