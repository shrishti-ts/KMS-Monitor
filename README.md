# 🖥️ KMS Monitor

A modular **Key Monitoring System** (for demo/testing only) that:

- ⌨️ Logs keystrokes locally
- 🔐 Encrypts logs using Fernet symmetric encryption
- 📧 Emails encrypted logs to a configured recipient
- 📊 Provides a Streamlit dashboard to view & decrypt logs

---

## 📁 Project Structure

Perfect! 💪
Let’s add the final two files to make your repo fully **publish-ready** on .

---

## 📁 `requirements.txt`

All dependencies your project needs to install.

```txt
pynput
cryptography
streamlit
pyyaml
```

> ✅ If you add tests later, you can also include `pytest` and `flake8` here.

---

## 📁 `README.md`

Clean and professional overview for your repository homepage.

```markdown
# 🖥️ KMS Monitor

A modular **Key Monitoring System** (for demo/testing only) that:

- ⌨️ Logs keystrokes locally
- 🔐 Encrypts logs using Fernet symmetric encryption
- 📧 Emails encrypted logs to a configured recipient
- 📊 Provides a Streamlit dashboard to view & decrypt logs

---

## 📁 Project Structure

```

kms-monitor/
├── kms.py
├── utils/
│   ├── logger.py
│   ├── crypto.py
│   └── sender.py
├── dashboard/
│   └── app.py
├── .github/workflows/ci.yml
├── docs/architecture.md
├── config\_template.yaml
├── requirements.txt
└── README.md

````

---

## ⚙️ Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/<shrishti-ts>/KMS-Monitor.git
   cd KMS-Monitor
````

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure secrets**
   Copy `config_template.yaml` ➜ `config.yaml` and fill in your:

   * `FERNET_KEY`
   * `SMTP_USER` / `SMTP_PASSWORD`
   * `SMTP_SERVER` and `PORT`

4. **Run the logger**

   ```bash
   python kms.py
   ```

5. **Run the dashboard**

   ```bash
   streamlit run dashboard/app.py
   ```

---

## 🛡️ Security & Ethics

> ⚠️ This project is for **educational purposes only**.
> Do **NOT** deploy, distribute, or use it to capture real user data without **explicit consent**.

---

## ✅ CI Integration

Each push/PR runs lint checks and tests automatically using .

---

## 📜 License

MIT License. See the [LICENSE](LICENSE) file for details.

```

\
