# utils/sender.py
import ssl
import smtplib
import os
import yaml

# Load config
with open("config_template.yaml", "r") as f:
    cfg = yaml.safe_load(f)

SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")

if not SMTP_USER or not SMTP_PASSWORD:
    raise ValueError("SMTP_USER or SMTP_PASSWORD not set in environment")

def send_email(message: str):
    """Send email securely using SMTP SSL."""
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(cfg['smtp_server'], cfg['smtp_port'], context=context) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(cfg['sender'], cfg['receiver'], message)
    print("Email sent successfully.")
