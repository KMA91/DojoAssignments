from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')

def counter():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 0

    return render_template('index.html')

@app.route('/asdf')

def button():

    if request.form['adder'] == "plus2":
        session['counter'] += 1

    return redirect('/')

@app.route('/abc')

def reset():

    session['counter'] = 0

    return redirect('/')

app.run(debug=True)