from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary Database
todos = [
    {"id": 1, "task": "Learn Flask"},
    {"id": 2, "task": "Build Todo App"}
]

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# View Todos Page
@app.route("/todos")
def view_todos():
    return render_template("todos.html", todos=todos)

# Add Todo
@app.route("/add", methods=["POST"])
def add_todo():

    task = request.form.get("task")

    if task:
        new_todo = {
            "id": len(todos) + 1,
            "task": task
        }
        todos.append(new_todo)

    return redirect(url_for("view_todos"))

# Delete Todo
@app.route("/delete/<int:id>")
def delete_todo(id):
    global todos
    todos = [todo for todo in todos if todo["id"] != id]

    return redirect(url_for("view_todos"))

# Update Todo
@app.route("/update/<int:id>", methods=["POST"])
def update_todo(id):

    updated_task = request.form.get("updated_task")

    for todo in todos:
        if todo["id"] == id:
            todo["task"] = updated_task
            break

    return redirect(url_for("view_todos"))


if __name__ == "__main__":
    app.run(debug=True)


'''
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Todo Storage
todos = [
    {"id": 1, "task": "Learn Flask"},
    {"id": 2, "task": "Build Todo App"}
]

# Home Page
@app.route("/")
def home():
    return render_template("index.html", todos=todos)

# Add Todo Page
@app.route("/add")
def add_todo_page():
    return render_template("add.html")

# Save Todo
@app.route("/save", methods=["POST"])
def save_todo():

    task = request.form.get("task")

    if task:
        new_todo = {
            "id": len(todos) + 1,
            "task": task
        }
        todos.append(new_todo)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
'''
