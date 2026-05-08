from flask import Flask, request, redirect
import json
import os

app = Flask(__name__)

FILE = "data.json"


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


# 🌐 HLAVNÍ STRÁNKA (UI)
@app.route("/")
def home():
    tasks = load_tasks()

    html_tasks = ""
    for t in tasks:
        html_tasks += f"""
        <li>
            {t['title']}
            <a href="/delete/{t['id']}" style="color:red;">❌</a>
        </li>
        """

    return f"""
    <h1>✅ To-Do App</h1>

    <form method="POST" action="/add">
        <input name="title" placeholder="Nový task..." required>
        <button type="submit">Přidat</button>
    </form>

    <h3>Seznam tasků:</h3>
    <ul>
        {html_tasks}
    </ul>
    """


# ➕ přidání tasku z formuláře
@app.route("/add", methods=["POST"])
def add():
    tasks = load_tasks()
    title = request.form.get("title")

    task = {
        "id": len(tasks) + 1,
        "title": title
    }

    tasks.append(task)
    save_tasks(tasks)

    return redirect("/")


# ❌ smazání tasku
@app.route("/delete/<int:task_id>")
def delete(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)

    return redirect("/")


if __name__ == "__main__":
    print("🚀 App běží na http://127.0.0.1:5000")
    app.run(debug=True)