from flask import Flask, request, redirect
import json
import os
from datetime import datetime

app = Flask(__name__)

FILE = "data.json"


# -------------------------
# DATA FUNKCE
# -------------------------
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


<<<<<<< HEAD
=======
def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


# -------------------------
# HLAVNÍ STRÁNKA
# -------------------------
>>>>>>> b454e52 (fix)
@app.route("/")
def home():
    tasks = load_tasks()

<<<<<<< HEAD
    task_items = ""
    for t in tasks:
        task_items += f"""
        <div class="task">
            <span>{t['title']}</span>
            <a href="/delete/{t['id']}" class="delete">✖</a>
        </div>
        """
=======
    active_html = ""
    done_html = ""

    for t in tasks:
        if t.get("done"):
            done_html += f"""
            <div class="task done">
                <a href="/toggle/{t['id']}">🔄</a>
                <span>{t['title']}</span>
                <small>{t.get('completed','')}</small>
                <a href="/delete/{t['id']}">✖</a>
            </div>
            """
        else:
            active_html += f"""
            <div class="task">
                <a href="/toggle/{t['id']}">⭕</a>
                <span>{t['title']}</span>
                <a href="/delete/{t['id']}">✖</a>
            </div>
            """
>>>>>>> b454e52 (fix)

    return f"""
    <html>
    <head>
        <title>To-Do App</title>
<<<<<<< HEAD
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
=======

        <style>
            body {{
                margin:0;
                font-family:Arial;
                background:#0f172a;
                color:white;
            }}

            .layout {{
                display:flex;
                height:100vh;
            }}

            .left,.right {{
                width:220px;
                background:#111827;
                padding:20px;
            }}

            .center {{
                flex:1;
                padding:20px;
            }}

            input {{
                padding:10px;
                border:none;
                border-radius:8px;
                width:70%;
            }}

            button {{
                padding:10px;
                border:none;
                border-radius:8px;
                background:#22c55e;
                color:white;
                cursor:pointer;
            }}

            .task {{
                background:#1f2937;
                padding:10px;
                margin-top:10px;
                border-radius:8px;
                display:flex;
                justify-content:space-between;
                align-items:center;
            }}

            .done {{
                opacity:0.5;
                text-decoration:line-through;
            }}

            a {{
                color:white;
                text-decoration:none;
                margin:0 5px;
            }}

            /* SETTINGS */
            .overlay {{
                display:none;
                position:fixed;
                top:0;
                left:0;
                width:100%;
                height:100%;
                background:rgba(0,0,0,0.8);
                justify-content:center;
                align-items:center;
            }}

            .panel {{
                background:#111827;
                padding:20px;
                border-radius:10px;
                width:350px;
            }}

            .option {{
                background:#1f2937;
                padding:10px;
                margin:8px 0;
                border-radius:8px;
                cursor:pointer;
            }}

            .option:hover {{
                background:#374151;
>>>>>>> b454e52 (fix)
            }}
        </style>
    </head>

    <body>
<<<<<<< HEAD
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
=======

    <div class="layout">

        <!-- LEFT -->
        <div class="left">
            <h3>📌 Menu</h3>
            <button onclick="openSettings()">⚙️ Nastavení</button>
        </div>

        <!-- CENTER -->
        <div class="center">
            <h2>📝 Úkoly</h2>

            <form method="POST" action="/add">
                <input name="title" placeholder="Nový úkol..." required>
                <button>Přidat</button>
            </form>

            <h3>Aktivní</h3>
            {active_html}

            <h3>Hotové</h3>
            {done_html}
        </div>

        <!-- RIGHT -->
        <div class="right">
            <h3>📊 Statistiky</h3>
            <div>🟡 Aktivní: {len([t for t in tasks if not t.get('done')])}</div>
            <div>✅ Hotové: {len([t for t in tasks if t.get('done')])}</div>
            <div>📦 Vše: {len(tasks)}</div>
        </div>

    </div>

    <!-- SETTINGS -->
    <div class="overlay" id="settings">
        <div class="panel">
            <h2>⚙️ Nastavení</h2>

            <div class="option">🔔 Notifikace</div>
            <div class="option">🎨 Téma</div>
            <div class="option">📊 Statistiky</div>
            <div class="option">🚀 Performance</div>

            <button onclick="closeSettings()">Zavřít</button>
        </div>
    </div>

    <script>
        function openSettings() {{
            document.getElementById("settings").style.display = "flex";
        }}

        function closeSettings() {{
            document.getElementById("settings").style.display = "none";
        }}
    </script>

>>>>>>> b454e52 (fix)
    </body>
    </html>
    """


<<<<<<< HEAD
=======
# -------------------------
# ADD TASK
# -------------------------
>>>>>>> b454e52 (fix)
@app.route("/add", methods=["POST"])
def add():
    tasks = load_tasks()

    tasks.append({
        "id": len(tasks) + 1,
        "title": request.form.get("title"),
        "done": False,
        "created": now(),
        "completed": None
    })

    save_tasks(tasks)
    return redirect("/")


<<<<<<< HEAD
=======
# -------------------------
# TOGGLE
# -------------------------
@app.route("/toggle/<int:task_id>")
def toggle(task_id):
    tasks = load_tasks()

    for t in tasks:
        if t["id"] == task_id:
            t["done"] = not t.get("done", False)
            t["completed"] = now() if t["done"] else None

    save_tasks(tasks)
    return redirect("/")


# -------------------------
# DELETE
# -------------------------
>>>>>>> b454e52 (fix)
@app.route("/delete/<int:task_id>")
def delete(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)

    return redirect("/")


# -------------------------
# START SERVER
# -------------------------
if __name__ == "__main__":
<<<<<<< HEAD
    print("🚀 Running on http://127.0.0.1:5000")
    app.run(debug=True)
=======
    print("🚀 Server běží na http://127.0.0.1:5000")
    app.run(debug=True)
>>>>>>> b454e52 (fix)
