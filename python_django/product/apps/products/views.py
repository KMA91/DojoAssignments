from django.shortcuts import render
from .models import Product

# Create your views here.

def index(request):
    Product.objects.create(name='iPhone', description='Cool phone', weight='3', price='200', cost='500', category='electronics')
    Product.objects.create(name='chair', description='made of wood', weight='10', price='100', cost='50', category='furniture')
    Product.objects.create(name='acer monitor', description='10 inch monitor', weight='5', price='125', cost='200', category='electronics')
    product = Product.objects.all()
    print product
    return render(request, 'products/index.html')
