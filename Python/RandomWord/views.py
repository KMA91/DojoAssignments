from django.shortcuts import render, redirect
# from random import choice

# Create your views here.
def index(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 0
    return render(request, 'RandomWord/index.html')
#
def generate(request):
    # print(request.method)
    # if request.method == 'POST':
    #     print FDJSFDSLKFJDSKLFJLKSDFJLKDSJFLK
    # else:
    #     pass
    return redirect('/asdf')
