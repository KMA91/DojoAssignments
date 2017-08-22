import re, md5
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import Flask, redirect, render_template, request, flash, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
mysql = MySQLConnector(app,'wall')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    wallDB = mysql.query_db('SELECT id, first_name, last_name, email, password FROM users')
    pass_log = md5.new(request.form['pass_log']).hexdigest()
    
    for infoDB in wallDB:
        if infoDB['email'] == request.form['email_log'] and infoDB['password'] == pass_log:
            session['id'] = infoDB['id']
            print session['id']
            return redirect ('/wall')
    flash('ERROR: Please register or TRY AGAIN!')
    return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    wallDB = mysql.query_db('SELECT email, password FROM users')
    fname = request.form['fname_reg']
    lname = request.form['lname_reg']
    passw = md5.new(request.form['pass_reg']).hexdigest();
    email_reg = request.form['email_reg']


    if len(fname) < 1 or len(lname) < 1 or len(email_reg) < 1 or  len(passw) < 1:
        flash('ERROR: You cannot leave any boxes empty!')
        return redirect('/')
    elif not EMAIL_REGEX.match(email_reg):
            flash('ERROR: Invalid EMAIL')
            return redirect ('/')
    else: 
        for infoDB in wallDB:
            if infoDB['email'] == email_reg:
                flash('ERROR: There is already an email like that in the database! Try again.')
            else:
                query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:fname, :lname, :email, :pword, now(), now())'
                data = {
                    'fname': fname,
                    'lname': lname,
                    'email': email_reg,
                    'pword': passw
                }

                mysql.query_db(query, data)
                return redirect('/')

@app.route('/wall')
def wall():
    wallDB = mysql.query_db('SELECT * FROM messages JOIN users ON messages.users_id = users.id')

    for infoDB in wallDB:
        session['fname'] = infoDB['first_name']
        session['lname'] = infoDB['last_name']
        session['message'] = infoDB['message']

    mess_dict = {
        'fname':session['fname'],
        'lname':session['lname'],
        'message':session['message']
    }

    return render_template('wall.html')

@app.route('/post', methods=['POST'])
def post():
    wallDB = mysql.query_db('SELECT * FROM messages JOIN users ON messages.users_id = users.id')
    query = 'INSERT INTO messages (users_id, message, created_at, updated_at) VALUES (:usersid, :messages, now(), now())'
    data = {
        'usersid': session['id'],
        'messages': request.form['postmsg']
    }

    for infoDB in wallDB:
        session['mes_time'] = infoDB['created_at']

    mysql.query_db(query, data)
    return redirect ('/wall')

app.run(debug=True)