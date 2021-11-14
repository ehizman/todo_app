from flask import render_template, request, redirect, url_for, jsonify, flash, session
from todo import db, app
from todo.models import Todo, Status


@app.route("/", methods=["GET"])
def display_todo():
    print("Hello in display todo")
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)


@app.route("/", methods=["POST"])
def add_todo():
    task = request.form.get("task")

    new_task = Todo(task=task)
    db.session.add(new_task)
    db.session.commit()

    flash("successfully added a new todo item", "green")
    return redirect(url_for("display_todo"))


@app.route("/delete/<todo_id>", methods=["GET"])
def delete_todo(todo_id):
    task_to_delete = Todo.query.get(todo_id)
    db.session.delete(task_to_delete)
    db.session.commit()

    flash("successfully deleted a todo item", "red")
    return redirect(url_for("display_todo"))


@app.route("/update/<todo_id>", methods=["GET"])
def update_todo_status(todo_id):
    task_to_update = Todo.query.get(todo_id)
    if task_to_update.status == Status.UNCOMPLETED:
        task_to_update.status = Status.COMPLETED
    else:
        task_to_update.status = Status.UNCOMPLETED
    db.session.commit()

    flash("successfully updated todo status", "green")
    return redirect(url_for("display_todo"))


@app.route("/update/<todo_id>", methods=["POST"])
def update_todo_task(todo_id):
    task = request.form.get("task")

    task_to_update = Todo.query.get(todo_id)
    task_to_update.task = task
    db.session.commit()

    return jsonify({
        "status": "success",
    }), 200


@app.route("/set-session/<data>", methods=["GET"])
def set_session(data):
    session["my-data"] = data

    return "Hello World!"


@app.route("/get-session", methods=["GET"])
def get_session():
    return session.get("my-data")
