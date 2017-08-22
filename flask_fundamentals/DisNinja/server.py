from flask import Flask, render_template
app = Flask(__name__)

@app.route ("/")

def index():
    return render_template('index.html')

@app.route("/ninja")
def ninja():
    
    show = True

    return render_template('ninja.html', show=show)

@app.route("/ninja/<color>")
def getcolor(color):
    show = False

    return render_template('ninja.html', color=color, show=show)


app.run(debug=True)