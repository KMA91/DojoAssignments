from django.shortcuts import render

# Create your views here.
def portfolio(request):
    return render(request, 'RealPortfolio/portfolio.html')

def projects(request):
    return render(request, 'RealPortfolio/projects.html')

def me(request):
    return render(request, 'RealPortfolio/me.html')

def testimonials(request):
    return render(request, 'RealPortfolio/testimonials.html')
