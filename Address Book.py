
from flask import Flask, render_template, redirect, request
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(host = "localhost", database = "mp3db", user = "root", password = "")
cur = conn.cursor()
print(cur)
print(conn)



@app.route('/')
def hello_world():
    return redirect('/index')

@app.route('/index')
def home():
    return render_template("homepage.html")


@app.route('/view')
def view():
    cur.execute("select * from addbook")
    contacts = cur.fetchall()
    #contacts = str(l)


    return render_template("view.html",  contacts =  contacts)


@app.route('/add')
def add():
    contact = {}
    return render_template("add.html", contact = contact)

@app.route('/new', methods = ['POST'])
def post():
    name = request.form["name"]
    phone = str(request.form["phoneNo"])
    email = request.form["email"]
    contact = {}
    contact["name"] = name
    contact['phone'] = phone
    contact["email"] = email


    query = "insert into addbook values(\'%s\', %d, \'%s\');" % (name, int(phone), email)
    cur.execute(query)
    return render_template("add.html", contact = contact)


if  __name__ == '__main__':
    app.run(debug=True)
