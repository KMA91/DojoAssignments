from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
   context = {
       'users' : User.objects.all()
   }

   return render(request, 'login/index.html', context)

def adduser(request):
    data = {
    'first': request.POST['fname'],
    'last': request.POST['lname'],
    'email': request.POST['email'],
    'password': request.POST['pword'],
    'passwordCON' : request.POST['pwordCON']
    }
    User.objects.register(data)
    results = User.objects(data)
######## THIS WILL USER:NONE AND ERRORS:(NUM OF ERRORS) IF THERE ARE ERRORS. THIS RUNS YOUR DATA INTO USERMANAGER ############

    if results['errors'] == None:
        request.session['user'] = results['user'].id
        return redirect ('/')
    else:
        for error in results['errors']:
            messages.add_message(request, messages.ERROR, error)
            return redirect('/')

    return redirect ('/')

def delete(request):
   User.objects.all().delete()
   return redirect('/')

# def success(request):
