from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Flask Basics<h1>"

@app.route("/api/greet/<name>")
def greet(name):
    return jsonify([
        {"message": f"Hello, {name}!"}
    ])


if __name__ == "__main__":
    app.run(debug=True)