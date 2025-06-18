import os
import requests
from flask import Flask
from main import run_tracker

app = Flask(__name__)

@app.route("/")
def home():
    return "Congress Tracker Bot is running."

@app.route("/run")
def run():
    return run_tracker()

@app.route("/ping")
def ping():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    message = "✅ 測試成功！你已成功收到來自 Billbilltracker_bot 的通知。"

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    r = requests.post(url, json=payload)
    return f"Status: {r.status_code}, {r.text}"

# ✅ 這一段是必要的！讓 Flask 綁定 Render 指定的 port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
