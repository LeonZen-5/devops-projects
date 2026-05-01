from flask import Flask, jsonify

app = Flask(__name__)

tasks = {}
next_id = 1


@app.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify(list(tasks.values()))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
