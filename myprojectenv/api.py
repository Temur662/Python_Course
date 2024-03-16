from flask import Flask
from flask import jsonify
app  = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

@app.route("/users")
def users():
    return jsonify([
        {
            "Name" : "Temur",
            "Age" : 19
        },
        {
        "Name" : "Mahmood",
        "Age" : 19
        }
    ])

    
if __name__ == "__main__":
    app.run(debug=True)