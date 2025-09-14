# 🧩 KMS Monitor – Architecture

## Overview
**KMS Monitor** is a modular key monitoring system that:
- Logs keystrokes locally
- Encrypts them with Fernet symmetric encryption
- Emails the encrypted logs securely via SMTP
- Provides a Streamlit dashboard to view & decrypt logs

---

## Directory Structure

kms-monitor/
├── kms.py
├── utils/
│ ├── logger.py
│ ├── crypto.py
│ └── sender.py
├── dashboard/
│ └── app.py
├── .github/workflows/ci.yml
├── docs/architecture.md
├── config_template.yaml
├── requirements.txt
└── README.md

---

## Flow

1. **Logging** – `kms.py` uses `pynput` to log keystrokes via `utils/logger.py`.
2. **Encryption** – Logs are encrypted using `utils/crypto.py` (:contentReference[oaicite:2]{index=2}).
3. **Email Sending** – Encrypted logs are sent to the configured recipient using `utils/sender.py` via :contentReference[oaicite:3]{index=3} SSL.
4. **Monitoring Dashboard** – `dashboard/app.py` provides a :contentReference[oaicite:4]{index=4} UI to view and decrypt uploaded logs.
5. **CI Pipeline** – `.github/workflows/ci.yml` runs lint checks and tests on each push.

---

## Secrets & Config

- **Environment Variables**
  - `FERNET_KEY` — Fernet symmetric key
  - `SMTP_USER` and `SMTP_PASSWORD` — Email credentials

- **config_template.yaml** (placeholders only, no secrets committed)

---

## Security Note
This project is for **educational purposes only**.  
Never deploy or use it to record keystrokes without **explicit user consent**.
