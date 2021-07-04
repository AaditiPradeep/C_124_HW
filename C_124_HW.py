from flask import Flask,jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'name': u'Raju',
        'contact': u'9823475698', 
        'done': False
    },
    {
        'id': 2,
        'name': u'Ram',
        'contact': u'9845761230', 
        'done': False
    }
]

@app.route("/") # local server 5000
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': tasks[-1]['id'] + 1,
        'name': request.json['name'],
        'contact': request.json.get('contact', ""), 
        'done': False
    }
    tasks.append(contact)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)