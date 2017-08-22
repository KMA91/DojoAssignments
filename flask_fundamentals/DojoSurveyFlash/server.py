from flask import Flask, render_template, redirect, request, flash

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

	if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
    else:
        flash("Success! Your name is{}".format(request.form['name']))
	return render_template('results.html', name=name, location=location, language=language, textarea=textarea)
	return redirect('/')

app.run(debug=True)