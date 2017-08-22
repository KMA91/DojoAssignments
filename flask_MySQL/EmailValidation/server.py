from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector(app,'email')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/val', methods=['POST'])
def val():
    emailDB = mysql.query_db('SELECT email FROM email')
    formemail = request.form['email']

    for email in emailDB:
        if not EMAIL_REGEX.match(formemail):
            return redirect ('/')
        if email['email'] == formemail:
            return redirect ('/')
        else:
            query = "INSERT INTO email (email, created_on) VALUE (:email, now())"
            data = {
                'email': formemail
            }
            session['emailSUCC'] = formemail
            mysql.query_db(query, data)
            return redirect ('/success')


@app.route('/success')
def suc():
    emaillist = mysql.query_db('SELECT * FROM email')
    return render_template('success.html', emails=emaillist)

app.run(debug=True)