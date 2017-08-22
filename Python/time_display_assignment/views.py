from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
import datetime

now = datetime.datetime.now()
# Create your views here.
def index(request):

    context = {
    "date": now
    }

    return render(request, 'time_display_assignment/index.html', context)
