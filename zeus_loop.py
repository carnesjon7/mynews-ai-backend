from flask import Flask
import threading
import time

app = Flask(__name__)

def zeus_loop():
    while True:
        print("🧠 Zeus is scanning for directives...")
        time.sleep(600)

@app.route("/")
def index():
    return "Zeus is live and watching."

@app.before_first_request
def activate_zeus():
    thread = threading.Thread(target=zeus_loop)
    thread.daemon = True
    thread.start()

if __name__ == "__main__":
    app.run()
