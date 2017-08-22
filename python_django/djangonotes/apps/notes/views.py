# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    # Post.objects.all().delete()
    context = {
    'posts': Post.objects.all()
    }

    return render(request, "notes/index.html", context)

def post(request):
    context = {
		'post': request.POST["post"],
        }
    Post.objects.post(context)

    context = {
        'posts': Post.objects.all()
    }
    return render(request, "notes/posts_index.html", context)
