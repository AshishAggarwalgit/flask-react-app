# Flask -> this is the main class to create flask app 
# it is basically used to create backend server
# request -> use to receive data from frontend
# jsonify -> use to convert python data into json as browser dont understand python list/dicts
# so we use jsonify

from flask import Flask, request, jsonify
# cors -> to establish communication between frontend and backend.
from flask_cors import CORS

# app is application object
# Flask() to tell server we creaitng flask app
# __name__ is to tell we are using current file as the main program file.
app = Flask(__name__)

# enable the cors for the app
# allow backend to access the backend api's
CORS(app)

# In-memory todo list

# create a python list to store all the todo's
# which will we array of object.
# example -> [{"id": 1, "task": "Shopping"}]
todos = []

# counter to give every todo a unique ID.
todo_id = 1


# Get all todos

# @-> this is the decorator which api with function
# app.route we use to create the route.
@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)


# Add new todo
@app.route("/todos", methods=["POST"])
def add_todo():
    # global -> we using global here to access variable outside function.
    # otherwise python will create new variable.
    global todo_id
    print(request, request.get_json())

    # check if request has the json
    if not request.is_json:
        return jsonify({"error": "Request must be json"}), 400

    # request -> get the request from frontend.
    # get_json() -> reading json body
    data = request.get_json()
    task = data.get("task")

    new_todo = {
        "id": todo_id,
        "task": task
    }

    todos.append(new_todo)
    todo_id += 1

    return jsonify(new_todo), 201


# Delete todo
# <int:id> -> takes dynamic value from url
#  if you want data of type string then it will be <string:id> or simply <id> as flask by default is string.
@app.route("/todos/<int:id>", methods=["DELETE"])
def delete_todo(id):
    global todos

# this we call list comprehension in python
# t is basically has all the element from array which satisfying condition.
    todos = [t for t in todos if t["id"] != id]

    return jsonify({"message": "Deleted"})  


# if current file is main file.
# here app.run() start the server
# and debug=True which runs the application in development mode.
# by default it runs on port 5000
if __name__ == "__main__":
    app.run(debug=True)