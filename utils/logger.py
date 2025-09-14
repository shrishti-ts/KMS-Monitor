# utils/logger.py
log_file = "keylogger.txt"

def write(text: str):
    """Append text to the keylogger file."""
    with open(log_file, 'a') as f:
        f.write(text)
