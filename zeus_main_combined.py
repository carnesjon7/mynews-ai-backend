
from flask import Flask
import threading
import time

app = Flask(__name__)

# Background loop for Zeus
def zeus_loop():
    print("⚡ Zeus Core Loop Activated...")
    while True:
        print("🧠 Zeus is scanning for directives...")
        time.sleep(600)  # Every 10 minutes

# Run loop when app starts
@app.before_first_request
def start_zeus():
    thread = threading.Thread(target=zeus_loop)
    thread.daemon = True
    thread.start()

@app.route("/")
def index():
    return "Zeus is live and watching."

# This line ensures it works on Render if using gunicorn zeus_main_combined:app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
