from flask import Flask, request, redirect, render_template, session
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'full_friends')

@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM users")
    return render_template('index.html', new_friends=friends)

@app.route('/friends', method="POST")
def create():
    query = "INSERT INTO users (name, age, friends_since) VALUES (:name, :age, now())"

    data = {
        'name': request.form['name'],
        'age': request.form['age']
    }

    mysql.query_db(query, data)

    return redirect('/')

app.run(debug=True)