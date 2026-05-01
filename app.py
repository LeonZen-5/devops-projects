from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = {}
next_id = 1


@app.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify(list(tasks.values()))


@app.route("/tasks", methods=["POST"])
def create_task():
    global next_id
    data = request.get_json()
    if not data or "description" not in data:
        return jsonify({"error": "description required"}), 400
    task = {"id": next_id, "description": data["description"], "done": False}
    tasks[next_id] = task
    next_id += 1
    return jsonify(task), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
