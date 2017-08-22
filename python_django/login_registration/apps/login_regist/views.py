# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Users
from django.contrib import messages

def index(request):
    context = {
        'users' : Users.objects.all()
    }
    print context
    return render(request, 'login_regist/index.html', context)

def adduser(request):
    context = {
        'first_name': request.POST['firstname'],
        'last_name': request.POST['lastname'],
        'email': request.POST['email'],
        'password': request.POST['password'],
        'confirm_password': request.POST['confirm_pass']
    }
    results = Users.objects.register(context)

    if results['errors'] == None:
        request.session['users'] = results['users'].id
        return redirect('/')
    else:
        for error in results['errors']:
            messages.add_message(request, messages.ERROR, error)
            return redirect('/')

    return redirect('/')

def success(request):
    context = {
    'email': request.POST['email'],
    'pword': request.POST['password']
    }

    results = Users.objects.login(context)

    if results['errors'] == None:
        return render(request, 'login_regist/success.html')
    else:
        for error in results['errors']:
            messages.add_message(request, messages.ERROR, error)
            return redirect('/')

    return render(request, 'login_regist/success.html', context)

def delete(request):
    Users.objects.all().delete()
    return redirect('/')
