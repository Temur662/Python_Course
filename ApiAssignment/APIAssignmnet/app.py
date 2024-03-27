from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def loadData():
    with open("data.json") as file:
        return json.load(file)

def saveData(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=2)

# Read/ GET
@app.route("/users", methods = ["GET"])
def getUsers():
    data = loadData()
    return jsonify(data["users"])

# Create/ POST
@app.route("/users", methods= ["POST"])
def addUser():
    if request.is_json:
        newUser = request.get_json()
        data = loadData()
        data["users"].append(newUser)
        saveData(data)
        return jsonify(newUser), 200
    return "Error must be a JSON request", 400

#Update/ PUT
@app.route("/users/<int:id>", methods = ["PUT"])
def updateUser(id):
    data = loadData()
    userIndex = 0
    for index, user in enumerate(data["users"]):
        if user["id"] == id:
            userIndex = index
            break
    
    if userIndex:
        updateData= request.get_json()
        user.update(updateData)
        data['users'][userIndex] = user
        saveData(data)
        return jsonify(user), 200
    return jsonify({"message":"Error user does not exist"}), 400

#Delete

@app.route("/users/<int:id>", methods = ["DELETE"])
def deleteUser(id):
    data = loadData()
    userIndex = 0
    userDict = 0
    for index, user in enumerate(data['users']):
        if user['id'] == id:
            userIndex = index
            userDict = user

    if userIndex:
        data['users'].pop(user)
        saveData(data)
        return(jsonify(userDict))
    else:
        return(jsonify({"message":"Error user not found"}))



if __name__ == "__main__":
    app.run(debug=True)