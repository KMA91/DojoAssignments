# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Users, Message, Likes
from django.contrib import messages


# FRONT PAGE #############################
def index(request):
    # Likes.objects.all().delete()
    context = {
        'users' : Users.objects.all(),
        'likes' : Likes.objects.filter(like=True)
    }
    return render(request, 'secrets/index.html', context)

# REGISTER ###################################
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
        request.session['users'] = results['users'].id
        return redirect('/')
    else:
        for error in results['errors']:
            messages.add_message(request, messages.ERROR, error)
            return redirect('/')

    return redirect('/')

# LOGIN #################################
def success(request):
    context = {
    'email': request.POST['email'],
    'pword': request.POST['password']
    }
    results = Users.objects.login(context)
    context = {
    'secrets': Message.objects.all().order_by('-created_at')[0:5]
    }
    if results['errors'] == None:
        request.session['name'] = results['name']
        request.session['id'] = results['userid']

        context= {
        'secrets': Message.objects.all().order_by('-created_at')[0:5],
        'count': Likes.objects.filter(like=True).count
        }
        return render(request, 'secrets/success.html', context)
    else:
        for error in results['errors']:
            messages.add_message(request, messages.ERROR, error)
            return redirect('/')

    return render(request, 'secrets/success.html', context)

def POSTsecret(request):
    context = {
    'secret': request.POST['secrethere'],
    'id': request.session['id']
    }
    results = Users.objects.secretPOSTER(context)
    context = {
    'secrets': Message.objects.all().order_by('-created_at')[0:5]
    }

    return render(request, 'secrets/success.html', context)

# DISPLAY POPULAR POSTS ###########################
def popular(request):
    context = {
    'popular': Messages.objects.all().order_by('')
    }

    return render(request, 'secrets/popular.html')

def like(request, id):
    context = {
    'POSTid': id,
    'userid': request.session['id']
    }
    results = Users.objects.likeCounter(context)
    context = {
    'secrets': Message.objects.all().order_by('-created_at')[0:5],
    }

    COUNT = results['count']

    return render(request, 'secrets/success.html', context, COUNT=COUNT)









def deletePOST(request):

    return render(request, 'secrets/success.html')


def delete(request):
    Users.objects.all().delete()
    return redirect('/')
