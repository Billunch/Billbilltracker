import os
from flask import Flask
from main import run_tracker

app = Flask(__name__)

@app.route("/")
def home():
    return "Congress Tracker Bot is running."

@app.route("/run")
def run():
    return run_tracker()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
