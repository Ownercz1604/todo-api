from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

FILE = "data.json"


# 🧠 bezpečné načítání (když soubor neexistuje nebo je prázdný)
def load_tasks():
    if not os.path.exists(FILE):
        return []

    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)


# 🌐 homepage
@app.route("/")
def home():
    return """
    <h1>✅ To-Do API běží</h1>
    <p>Použij:</p>
    <ul>
        <li>GET /tasks</li>
        <li>POST /tasks</li>
        <li>DELETE /tasks/&lt;id&gt;</li>
    </ul>
    """


# 📋 get tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(load_tasks())


# ➕ add task
@app.route("/tasks", methods=["POST"])
def add_task():
    tasks = load_tasks()
    data = request.json

    if not data or "title" not in data:
        return jsonify({"error": "Missing title"}), 400

    task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "done": False
    }

    tasks.append(task)
    save_tasks(tasks)

    return jsonify(task)


# ❌ delete task
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)

    return jsonify({"message": "deleted"})


# 🚀 start server
if __name__ == "__main__":
    print("🚀 Server běží na http://127.0.0.1:5000")
    app.run(debug=True, host="127.0.0.1", port=5000)