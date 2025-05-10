
from flask import Flask
import threading
import time

app = Flask(__name__)

# Background loop for Zeus
def zeus_loop():
    print("⚡ Zeus Core Loop Activated...")
    while True:
        print("🧠 Zeus is scanning for directives...")
        time.sleep(600)

# Run loop when app starts
def start_zeus():
    thread = threading.Thread(target=zeus_loop)
    thread.daemon = True
    thread.start()

@app.before_first_request
def initialize():
    start_zeus()

@app.route("/")
def index():
    return "Zeus is live and watching."

# Trigger loop when using gunicorn (Render production mode)
if __name__ != "__main__":
    start_zeus()

# For local development only
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
