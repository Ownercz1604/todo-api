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


@app.route("/")
def home():
    tasks = load_tasks()

    task_items = ""
    for t in tasks:
        task_items += f"""
        <div class="task">
            <span>{t['title']}</span>
            <a href="/delete/{t['id']}" class="delete">✖</a>
        </div>
        """

    return f"""
    <html>
    <head>
        <title>To-Do App</title>
        <style>
            body {{
                font-family: Arial;
                background: #0f172a;
                color: white;
                display: flex;
                justify-content: center;
                padding-top: 50px;
            }}

            .container {{
                width: 400px;
                background: #111827;
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0 0 20px rgba(0,0,0,0.5);
            }}

            h1 {{
                text-align: center;
                margin-bottom: 20px;
            }}

            form {{
                display: flex;
                gap: 10px;
            }}

            input {{
                flex: 1;
                padding: 10px;
                border-radius: 8px;
                border: none;
                outline: none;
            }}

            button {{
                padding: 10px 15px;
                border: none;
                border-radius: 8px;
                background: #22c55e;
                color: white;
                cursor: pointer;
            }}

            button:hover {{
                background: #16a34a;
            }}

            .task {{
                background: #1f2937;
                padding: 10px;
                margin-top: 10px;
                border-radius: 10px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                transition: 0.2s;
            }}

            .task:hover {{
                transform: scale(1.02);
            }}

            .delete {{
                color: red;
                text-decoration: none;
                font-size: 18px;
            }}

            .delete:hover {{
                color: #ff4d4d;
            }}
        </style>
    </head>

    <body>
        <div class="container">
            <h1>📝 To-Do App</h1>

            <form method="POST" action="/add">
                <input name="title" placeholder="Napiš úkol..." required>
                <button type="submit">Přidat</button>
            </form>

            <div style="margin-top:20px;">
                {task_items}
            </div>
        </div>
    </body>
    </html>
    """


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


@app.route("/delete/<int:task_id>")
def delete(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)

    return redirect("/")


if __name__ == "__main__":
    print("🚀 Running on http://127.0.0.1:5000")
    app.run(debug=True)
