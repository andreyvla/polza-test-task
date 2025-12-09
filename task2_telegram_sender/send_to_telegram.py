#!/usr/bin/env python3
"""
Simple Telegram sender for Polza test task.

Usage:
    python send_to_telegram.py message.txt

- Reads text from a given .txt file
- Sends this text to a private Telegram chat via a bot
"""

import sys
import os
import requests


def main() -> None:
    # Check CLI args
    if len(sys.argv) < 2:
        print("Usage: python send_to_telegram.py <text_file>")
        sys.exit(1)

    text_file = sys.argv[1]

    # Read Telegram token & chat ID from environment variables
    token = os.environ.get("TG_BOT_TOKEN")
    chat_id = os.environ.get("TG_CHAT_ID")

    if not token or not chat_id:
        print("Error: please set TG_BOT_TOKEN and TG_CHAT_ID environment variables.")
        sys.exit(1)

    # Read message from file
    try:
        with open(text_file, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: file '{text_file}' not found.")
        sys.exit(1)

    if not text.strip():
        print("Warning: message file is empty. Nothing to send.")
        sys.exit(0)

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": text,
    }

    try:
        response = requests.post(url, data=payload, timeout=5)
    except requests.RequestException as e:
        print("Error sending message:", e)
        sys.exit(1)

    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print("Error sending message:", response.status_code, response.text)


if __name__ == "__main__":
    main()