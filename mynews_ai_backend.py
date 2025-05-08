# Entry point for your Flask app
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'MyNews AI is live.'