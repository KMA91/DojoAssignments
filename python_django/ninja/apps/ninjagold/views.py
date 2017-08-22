from django.shortcuts import render, redirect
import random, datetime

# Create your views here.
def index(request):
    try:
        request.session['gold']
    except:
        request.session['gold'] = 0
    try:
        request.session['activity']
    except:
        request.session['activity'] = []
    return render(request, 'ninjagold/index.html')

def process(request):
    if request.POST['location'] == 'farm':
        earned_gold = random.randrange(10,21)
        request.session['gold'] += earned_gold
        new_activity = 'Earned '+ str(earned_gold)+ ' golds from the farm!'+ '('+ str(datetime.datetime.now())+')'
        new_dict = {
        'message':new_activity
        }
        request.session['activity'].append(new_dict)
    elif request.POST['location'] == 'cave':
        earned_gold = random.randrange(5,11)
        request.session['gold'] += earned_gold
        new_activity = 'Earned '+ str(earned_gold)+ ' golds from the cave!'+ '('+ str(datetime.datetime.now())+')'
        new_dict = {
        'message':new_activity
        }
        request.session['activity'].append(new_dict)
    elif request.POST['location'] == 'house':
        earned_gold = random.randrange(2,6)
        request.session['gold'] += earned_gold
        new_activity = 'Earned '+ str(earned_gold)+ ' golds from the house!'+ '('+ str(datetime.datetime.now())+')'
        new_dict = {
        'message':new_activity
        }
        request.session['activity'].append(new_dict)
    elif request.POST['location'] == 'casino':
        earned_gold = random.randrange(-50,51)
        request.session['gold'] += earned_gold
        if earned_gold > 0:
            new_activity = 'Earned '+ str(earned_gold)+ ' golds from the casino!'+ '('+ str(datetime.datetime.now())+')'
            new_dict = {
            'message':new_activity
            }
            request.session['activity'].append(new_dict)
        else:
            new_activity = 'Entered a casino and lost '+ str(-earned_gold)+ ' golds...Ouch..'+'(' + str(datetime.datetime.now())+')'
            new_dict = {
            'message': new_activity
            }
            request.session['activity'].append(new_dict)
    return redirect('/')
