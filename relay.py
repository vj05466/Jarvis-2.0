import requests

TOKEN = "8176018284:AAE6mzLoZgKsCAdcKDrIZCNR9ngAzpQKzzs"
CHAT_ID = "@Jarvis_2_o_bot"  # or use numeric ID if this fails

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    try:
        res = requests.post(url, json=payload)
        return res.json()
    except Exception as e:
        print("Telegram Error:", e)# This is a placeholder for relay.py
