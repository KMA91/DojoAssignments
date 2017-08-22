from flask import Flask, render_template, redirect, session, request
import random, datetime
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')
def index():
    try:
        session["gold"]
    except:
        session["gold"] = 0
    try:
        session["activities"]
    except:
        session["activities"] = []

    return render_template('index.html')

@app.route('/process_money', methods=["POST"])
def get_gold():

    if request.form["location"] == "farm":
        earned_gold = random.randrange(10,21)
        session["gold"] += earned_gold
        new_activity = "Earned "+ str(earned_gold)+ " from the "+ request.form["location"]+ "!"+ "("+str(datetime.datetime.now())+")"    
        new_dict = {
        'message':new_activity,
        'won':True
        }
        session["activities"].append(new_dict)      
    elif request.form["location"] == "cave":
        earned_gold = random.randrange(5,11)
        session["gold"] += earned_gold
        new_activity = "Earned "+ str(earned_gold)+ " from the "+ request.form["location"]+ "!"+ "("+str(datetime.datetime.now())+")"
        new_dict = {
        'message':new_activity,
        'won':True
        }
        session["activities"].append(new_dict)               
    elif request.form["location"] == "house":
        earned_gold = random.randrange(2,6)
        session["gold"] += earned_gold
        new_activity = "Earned "+ str(earned_gold)+ " from the "+ request.form["location"]+ "!"+ "("+str(datetime.datetime.now())+")"
        new_dict = {
        'message':new_activity,
        'won':True
        }
        session["activities"].append(new_dict)           
    elif request.form["location"] == "casino":
        earned_gold = random.randrange(-50,51)
        session["gold"] += earned_gold
        if earned_gold > 0:
            new_activity = "Earned "+ str(earned_gold)+ " from the "+ request.form["location"]+ "!"+ "("+str(datetime.datetime.now())+")"
            won = True
        else:
            new_activity = "Entered a casino and lost "+ str(-earned_gold)+ " golds... Ouch.."+ "("+str(datetime.datetime.now())+")"
            won = False
        new_dict = {
        'message':new_activity,
        'won':won
        }
        session["activities"].append(new_dict)        
    return redirect ('/')

app.run(debug=True)