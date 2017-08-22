from django.shortcuts import render
# Create your views here.

def index(request):

    return render(request, 'SurveyForm/index.html')

def results(request):
    return render(request, 'SurveyForm/results.html')
