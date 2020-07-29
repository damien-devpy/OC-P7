from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Welcome on the GranPy chatbot !</h1>"
