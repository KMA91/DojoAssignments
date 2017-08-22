# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Users, Message, Likes
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "secrets/index.html")

def register(request):
    context = {
        'first_name': request.POST['firstname'],
        'last_name': request.POST['lastname'],
        'email': request.POST['email'],
        'password': request.POST['password'],
        'confirm_password': request.POST['confirm_pass']
    }

    results = Users.objects.register(context)

    if results['errors'] == None:
        return redirect('/')
    else:
        for error in results['errors']:
            messages.add_message(request, messages.ERROR, error)
            return redirect('/')

    return redirect('/')

def login(request):

    try:
        context = {
        'email': request.POST['email'],
        'pword': request.POST['password']
        }
        results = Users.objects.login(context)

        if results['errors'] == None:
            request.session['name'] = results['name']
            request.session['id'] = results['userid']
            return render(request, 'secrets/success.html', context)
        else:
            for error in results['errors']:
                messages.add_message(request, messages.ERROR, error)
                return redirect('/')
    except:
        return render(request, 'secrets/success.html')

def addsecret(request):
    context = {
    "secret": request.POST["secrethere"],
    "user_id": request.session["id"],
    }
    Users.objects.postsecret(context)


    return request(render, 'secrets/success.html')
