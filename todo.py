
from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:////Users/ismai/OneDrive/Masaüstü/TODO_APP/todo.db"
db=SQLAlchemy(app)
@app.route("/")
def index():
    todos = Todo.query.all()


    return render_template("index.html",todos=todos)


@app.route("/complete/<string:id>")
def completetodo(id):

    todo=Todo.query.filter_by(id=id).first()
    if todo.complete==True:
        todo.complete=False
    else:
        todo.complete==False
        todo.complete=True
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/add",methods=["POST"])
def addtodo():
    title=request.form.get("title")   
    newtodo=Todo(title=title,complete=False)
    db.session.add(newtodo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def DeleteTodo(id):
    todo=Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

  
class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(80))
    complete=db.Column(db.Boolean)
 
    

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
