# Entry point for your Flask app
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'MyNews AI is live.'
# Don't include app.run() anymore
# Just define 'app' like this at the top of the file:
# from flask import Flask
# app = Flask(__name__)

# Nothing else needed at the bottom
