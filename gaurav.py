from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory database (a dictionary) for storing tasks
tasks = {}

# Task ID counter
task_id_counter = 1

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    return jsonify(list(tasks.values()))

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Get a specific task by ID"""
    task = tasks.get(task_id)
    if task is None:
        abort(404)  # Task not found
    return jsonify(task)

@app.route('/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    global task_id_counter
    data = request.json
    task_id = task_id_counter
    task = {
        'id': task_id,
        'title': data['title'],
        'completed': False
    }
    tasks[task_id] = task
    task_id_counter += 1
    return jsonify(task), 201  # 201 Created

@app.route('/tasks/<int:task_id>', methods=['PATCH'])
def update_task(task_id):
    """Update a task by ID"""
    task = tasks.get(task_id)
    if task is None:
        abort(404)  # Task not found

    data = request.json
    if 'title' in data:
        task['title'] = data['title']
    if 'completed' in data:
        task['completed'] = data['completed']
    
    tasks[task_id] = task
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task by ID"""
    task = tasks.get(task_id)
    if task is None:
        abort(404)  # Task not found
    
    del tasks[task_id]
    return '', 204  # 204 No Content

if __name__ == '__main__':
    app.run(debug=True)
