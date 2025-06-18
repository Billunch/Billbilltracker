from flask import Flask
from main import run_tracker

app = Flask(__name__)

@app.route("/")
def home():
    return "Congress Tracker Bot is running."

@app.route("/run")
def run():
    return run_tracker()
