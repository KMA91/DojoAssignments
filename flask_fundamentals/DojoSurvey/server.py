from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')

def index():
	return render_template ('index.html')

@app.route('/results', methods=['POST'])

def results():
	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	textarea = request.form['textarea']
	return render_template('results.html', name=name, location=location, language=language, textarea=textarea)
	return redirect('/')

@app.route('/results')

def form():
	return render_template('results.html')

app.run(debug=True)