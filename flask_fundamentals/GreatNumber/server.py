import random

from flask import Flask, flash, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
    if 'setNum' not in session:
        session['setNum'] = random.randint(1,100)
    return render_template('index.html')

@app.route('/number', methods = ["POST"])
def guessCheck():
    numGuess = int(request.form['numGuess'])
    answer = int(session['setNum'])
    correct = False

    if numGuess == answer:
        phrase = "{0} was the number".format(answer)
        correct = True
    elif numGuess < answer:
        phrase = "Too low!"
    elif numGuess > answer:
        phrase = "Too high!"
    
    session['phrase'] = phrase
    session['correct'] = correct

    return redirect ('/')


    
app.run(debug=True)