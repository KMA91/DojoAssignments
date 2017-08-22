from django.shortcuts import render, redirect
from .models import Book

# Create your views here.
def index(request):
    context = {
    'book': Book.objects.all()
    # select * from Books
    }

    return render(request, 'FSBooks/index.html', context)

def add(request):
    Book.objects.create(title=request.POST['title'], author=request.POST['author'], category=request.POST['category'])
    # insert into BookDB
    return redirect('/')
