"""
tipsy.py -- A flask-based todo list
"""
from flask import Flask, render_template, request, redirect, session, url_for, escape
import model_ar

app = Flask(__name__) #Flask is capitalized because it is a class. Name is name of file

@app.route("/") #tells Flask what url is attached to this function, this one is 'http://localhost:5000/''
def index():
    # return "<html><body>Woo I'm tipsy</body></html>" #decorated function
    return render_template("index.html", user_name="chriszf")

@app.route("/tasks")
def list_tasks():
    db = model_ar.connect_db() # connect to database
    tasks_from_db = model_ar.get_tasks(db, )  #gets a list of all tasks
    return render_template("list_tasks.html", tasks=tasks_from_db) 
    # send that list to the list_tasks.html template as a parameter named 'tasks'

# @app.route("/new_task")
# def new_tasks():
#     return render_template("new_task.html")

@app.route("/save_task", methods=["POST"])
def save_task():
    task_title = request.form['task_title']
    db = model_ar.connect_db()
    #Assume all tasks are attached to user 1.
    task_id = model_ar.new_task(db, task_title, 1)
    return redirect("/tasks")

# @app.route("/completed_task")
# def completed_task():
#     return render_template("completed_task.html")

@app.route("/done_task", methods=["POST"])
def save_complete():
    timestamp = request.form['task_complete']
    db = model_ar.connect_db()
    task_query = model_ar.complete_task(db, timestamp)
    return redirect("/tasks")

if __name__ == "__main__":  #Starts application when we run our program from command line
    app.run(debug=True)
