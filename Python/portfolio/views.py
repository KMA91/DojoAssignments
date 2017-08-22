from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def testimonials(request):
    return render(request, 'testimonials.html')
