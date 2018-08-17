from flask import Flask, request, jsonify, json
from flask_pymongo import PyMongo
from bson.json_util import dumps,ObjectId

app= Flask(__name__)
app.config['MONGO_DBNAME']='axiom'
app.config['MONGO_URI']='mongodb://ali:ali123@ds237947.mlab.com:37947/axiom'
mongo = PyMongo(app)




@app.route("/",methods=["GET"])
def index():
    todo= mongo.db.todo

    output =[]

    for todos in todo.find():
        id = json.loads(dumps(todos['_id']))

        # todo_data['text'] = todo.text
        # todo_data['complete'] = todo.complete
        output.append({'_id': id["$oid"],
                       'title': todos['title'],
                       'description':todos['description'],
                       'complete':todos['complete']})

    return jsonify({'todos': output})
@app.route("/todo/<id>",methods=["GET"])
def get_one(id):
    todos= mongo.db.todo

    todo = todos.find_one({"_id":ObjectId(id)})
    if todo:
        output=[]
        output.append({"_id":id,
                       "title":todo["title"],
                       "description":todo["description"],"complete":todo["complete"]})
    else:
        output= "Nothing Found"
    return jsonify({"results ":output})


@app.route('/todo', methods=['POST'])
def create_todo():
    todos= mongo.db.todo

    title = request.json["title"]
    description= request.json["description"]

    id=todos.insert({"title":title ,"description":description ,"complete":False})
    new_todo=todos.find_one({'_id':id})
    output={'title':new_todo['title'],
            'complete':new_todo['complete']}


    return jsonify(output)


@app.route('/todo/<id>',methods=['PUT'])
def update(id):
    todos = mongo.db.todo

    todo = todos.find_one({"_id": ObjectId(id)})
    output =[]
    if todo:
     todo["complete"]=True
     todos.save(todo)
     output="Task Done "
    else:
        output ="Nothing"


    return jsonify({"Result ":output})
@app.route("/todo/<id>",methods=["DELETE"])
def delete(id):
    todos = mongo.db.todo
    todo = todos.delete_one({"_id": ObjectId(id)})

    return jsonify("Deleted")



app.run(debug=True)
