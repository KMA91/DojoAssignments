from django.shortcuts import render, redirect
# Create your views here.

def index(request):
    return render(request, 'surveyform/index.html')

def results(request):
    if request.method == 'POST':
        if 'counter' in request.session:
            request.session['counter'] += 1
        else:
            request.session['counter'] = 1
        request.session['name'] = request.POST['name']
        request.session['favlang'] = request.POST['language']
        request.session['location'] = request.POST['location']
        request.session['option'] = request.POST['textarea']
    return render(request, 'surveyform/results.html')
