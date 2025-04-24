from flask import Flask, request
from relay import send_telegram_message

app = Flask(__name__)

@app.route('/')
def home():
    return "Jarvis Backend Running..."

@app.route('/result', methods=['POST'])
def handle_result():
    data = request.get_json()
    if data:
        color = data.get("color")
        timestamp = data.get("timestamp")
        if color:
            message = f"Color: {color}\nTime: {timestamp}"
            send_telegram_message(message)
            return {"status": "sent"}
    return {"error": "Invalid data"}, 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)# This is a placeholder for main.py
