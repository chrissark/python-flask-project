from flask import Flask, render_template, request, redirect, url_for

from database import DataBase
from tools import Task

app = Flask(__name__)

HOST = 'redis'
PORT = 6379

db = DataBase(host=HOST, port=PORT)


@app.route("/")
def index():
    tasks_dict = db.get_all_tasks()
    return render_template("index.html", list_of_tasks=tasks_dict)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get('title')
    if title:
        new_task = Task(title)
        db.add_task_to_db(new_task)
    return redirect(url_for('index'))


@app.route("/delete/<int:task_id>")
def delete(task_id):
    db.remove_task_by_idx(task_id)
    return redirect(url_for('index'))


@app.route("/update/<int:task_id>")
def complete(task_id):
    db.modify_task_by_idx(task_id)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()
