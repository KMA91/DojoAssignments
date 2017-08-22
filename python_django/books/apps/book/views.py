from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    Book.objects.create(title='Harry Potter', author='J.K Rowling', category='sci-fi')
    Book.objects.create(title='7 Habits', author='author2', category='educational')
    Book.objects.create(title='Book3', author='author3', category='bookcategory3')
    Book.objects.create(title='Book4', author='author4', category='bookcategory4')
    Book.objects.create(title='Book5', author='author5', category='bookcategory5')
    book = Book.objects.all()
    print book
    return render(request, 'book/index.html')
