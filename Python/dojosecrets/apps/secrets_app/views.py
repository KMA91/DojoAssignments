# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Secret
from django.db.models import Count
import datetime


# Create your views here.
def index(request):
    return render(request, 'secrets_app/index.html')

def register(request):
    context = {
    'fname': request.POST['first_name'],
    'lname': request.POST['last_name'],
    'pw': request.POST['password'],
    'conf_pw': request.POST['confirm_password'],
    'em': request.POST['email'],
    'dob': request.POST['birthdate']
    }
    regResults = User.objects.validateReg(context)

    if regResults['new'] != None:
        request.session['user_id'] = regResults['new'].id
        request.session['user_firstname'] = regResults['new'].first_name
        return redirect('/success')
    else:
        for error_str in regResults['error_list']:
            messages.add_message(request, messages.ERROR, error_str)
        return redirect('/')

def success(request):
    if 'user_id' not in request.session:
        messages.add_message(request, messages.ERROR, 'You must be logged in to view that page.')
        return redirect('/')
    else:
        recent_secrets = Secret.objects.all().order_by('-id')[:5]
        print recent_secrets
        context = {
        'recent_secrets': recent_secrets
        }
        return render(request, 'secrets_app/secrets.html', context)

def login(request):
    userLog = {
        'loginEmail': request.POST['email'],
        'loginPw': request.POST['password']
    }

    login_results = User.objects.userLogin(userLog)

    if login_results['list_errors'] != None:
        for error in login_results['list_errors']:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/')
    else:
        request.session['user_id'] = login_results['logged_user'].id
        request.session['user_firstname'] = login_results['logged_user'].first_name
        return redirect ('/success')

def logout(request):
	request.session.clear()
	return redirect('/')

def popularsecret(request):
    context = {
    'popular_secrets': Secret.objects.annotate(num_likes=Count('likes')).order_by('-num_likes'),
    }
    return render(request, 'secrets_app/popularsecrets.html', context)

def postsecret(request):
    context = {
    "secretuser": int(request.session['user_id']),
    "secretmsg": request.POST['secret']
    }
    validation = Secret.objects.add_secret(context)

    return redirect('/success')

def likesecret(request, id):
    like_id = int(id)
    like_user = User.objects.get(id=request.session['user_id'])
    like_secret = Secret.objects.get(id=like_id)
    context = {
    "secretuser": int(request.session['user_id']),
    "secretid": like_id
    }
    validation = Secret.objects.like_secret(context)

    return redirect('/success')

def deletesecret(request, id):
    delete_id = id
    context = {
    "secretuser": int(request.session['user_id']),
    "secretid": delete_id
    }
    validation = Secret.objects.delete_secret(context)
    return redirect('/success')
