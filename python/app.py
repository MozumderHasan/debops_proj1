from flask import Flask, render_template, request, redirect
import mysql.connector
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()
# MySQL Configuration
db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
# db = mysql.connector.connect(
#     user='root', password='root', host='mysql', port="8888", database='infodb')
# print("DB connected")

@app.route("/")
def index():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template("index.html", users=users)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        cursor = db.cursor()
        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        values = (name, email)
        cursor.execute(query, values)
        db.commit()
        return redirect("/")
    else:
        return render_template("add.html")
    

@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def update(id):
    id=int(id)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE id = {}".format(id))
    user = cursor.fetchone()
    context={
        'user':user
    }
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        query = "UPDATE users SET name = %s, email = %s WHERE id = %s"
        values = (name, email, id)
        cursor.execute(query, values)
        db.commit()
        return redirect("/")
    else:
        return render_template("update.html",**context)


@app.route("/delete/<int:id>")
def delete(id):
    cursor = db.cursor()
    query = "DELETE FROM users WHERE id = %s"
    values = (id,)
    cursor.execute(query, values)
    db.commit()
    return redirect("/")



if __name__ == "__main__":
    app.run()