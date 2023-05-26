from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True)

    def __init__(self, title):
        self.title = title

class TaskSchema(ma.Schema):
    class Meta:
        fields = ('title', 'id')

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

@app.route('/task', methods=['POST'])
def add_task():
    title = request.json['title']
    new_task = Task(title)
    db.session.add(new_task)
    db.session.commit()
    return task_schema.jsonify(new_task)

@app.route('/task', methods=['GET'])
def get_tasks():
    all_tasks = Task.query.all()
    result = tasks_schema.dump(all_tasks)
    return jsonify(result)

@app.route('/task/<id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get(id)
    title = request.json['title']
    task.title = title
    db.session.commit()
    return task_schema.jsonify(task)

@app.route('/task/<id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return task_schema.jsonify(task)

if __name__ == '__main__':
    app.run(debug=True)
