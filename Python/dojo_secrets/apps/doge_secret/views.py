# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count
from .models import Users, Posts, Likes

def index(request):
    context = {
        'users' : Users.objects.all()
    }
    return render(request, 'doge_secret/index.html', context)

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
        request.session['users_id'] = results['users'].id
        request.session['users_name'] = results['users'].first_name
        return redirect('/secrets')
    else:
        for error in results['errors']:
            messages.add_message(request, messages.ERROR, error)
            return redirect('/')

def login(request):
    context = {
        'email': request.POST['email'],
        'password': request.POST['password'],
    }
    results = Users.objects.login(context)

    if results['errors'] == None:
        request.session['users_id'] = results['users'].id
        request.session['users_name'] = results['users'].first_name
        return redirect('/secrets')
    else:
        for error in results['errors']:
            messages.add_message(request, messages.ERROR, error)
            return redirect('/')

def secrets(request):
    current_user = Users.objects.get(id=request.session['users_id'])
    all_posts = Posts.objects.all().order_by('-created_at')[0:5]
    user = request.session['users_id']
    name = Users.objects.get(id=user).first_name
    post_list = []
    for post in all_posts:
        post.liked = True
        post.num_likes = Likes.objects.filter(post_id=post).count()
        try:
            Likes.objects.get(user_id=current_user, post_id=post)
        except:
            post.liked = False
        post_list.append(post)

    context = {
    'first_name': name,
    'all_posts': all_posts,
    'likes': Likes.objects.all().count(),
    'posts': post_list
    }
    return render(request, 'doge_secret/secrets.html', context)

def post(request):
    user_id = Users.objects.get(id=request.session['users_id'])
    context = {
        'id': user_id,
        'posts' : request.POST['posts']
    }
    Posts.objects.post(context)
    return redirect('/secrets')

def like(request, post_id):
    posts = Posts.objects.get(id=post_id)
    users = Users.objects.get(id=request.session['users_id'])
    context = {
        'post_id': posts,
        'user_id': users,
    }
    Likes.objects.like(context)
    return redirect('/secrets')

def destroy_post(request, post_id):
	posts = Posts.objects.get(id=post_id)
	if posts.user_id.id == request.session['users_id']:
        #user_id is under Posts Mananger
		posts.delete()
	else:
		messages.add_message(request, messages.ERROR, "You're not allowed to do that")
	return redirect('/secrets')

def pop_secrets(request):
    current_user = Users.objects.get(id=request.session['users_id'])
    all_posts = Posts.objects.annotate(num_likes=Count('secret_likes')).order_by('-num_likes')
    # user = request.session['users_id']
    # name = Users.objects.get(id=user).first_name
    post_list = []

    for post in all_posts:
        post.liked = True
        post.num_likes = Likes.objects.filter(post_id=post).count()
        try:
            Likes.objects.get(user_id=current_user, post_id=post)
        except:
            post.liked = False
        post_list.append(post)

    context = {
    # 'first_name': name,
    'all_posts': all_posts,
    'likes': Likes.objects.all().count(),
    'posts': post_list
    }
    return render(request, 'doge_secret/pop_secrets.html', context)

def back(request):
    return redirect('/secrets')

def logout(request):
    request.session.clear()
    return redirect ('/')
