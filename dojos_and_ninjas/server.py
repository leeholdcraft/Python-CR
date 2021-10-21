from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route("/")
def index():
    mysql = connectToMySQL('dojos_and_ninjas')
    dojos = mysql.query_db('SELECT * FROM dojos;')
    print(dojos)
    return render_template("home.html", all_dojos=dojos)

@app.route("/dojos", methods=['POST'])
def create():
    mysql = connectToMySQL('dojos_and_ninjas')
    query = "INSERT INTO dojos (name, created_at, updated_at) VALUES ((%(name)s), NOW(), NOW());"
    print("test")
    data = {
        "name": request.form["name"],
    }
    dojos=mysql.query_db(query,data)
    print(dojos)
    return redirect("/")

@app.route('/display/<dojos_id>')
def show(dojos_id):
    mysql = connectToMySQL('dojos_and_ninjas')
    data = {
        "id": dojos_id
    }
    ninjas = mysql.query_db("SELECT * FROM ninjas JOIN dojos ON ninjas.dojos_id = dojos.id WHERE ninjas.dojos_id = %(id)s;", data)
    return render_template("show.html", all_ninjas=ninjas)

@app.route("/create")
def display():
    mysql = connectToMySQL('dojos_and_ninjas')
    dojos = mysql.query_db('SELECT * FROM dojos;')
    print(dojos)
    return render_template("addnew.html", dojos=dojos)

@app.route("/addnewninja", methods=['POST'])
def addnew():
    mysql = connectToMySQL('dojos_and_ninjas')
    query = "INSERT INTO ninjas (first_name, last_name, age, dojos_id, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojos_id)s, NOW(), NOW());"
    data = {
        "dojos_id": request.form["dojos_id"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
    }
    ninjas =mysql.query_db(query,data)
    print(ninjas)
    return redirect('/')
            
if __name__ == "__main__":
    app.run(debug=True)
