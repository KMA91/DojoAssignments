# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UsersManager(models.Manager):
    def register(self, data):
        errors=[]

        if data['first_name'] == "":
            errors.append('first name cannot be blank')
        elif len(data['first_name']) < 2:
            errors.append('first name cannot be fewer than 2 characters')
        if not data['first_name'].isalpha():
            errors.append('first name must only be characters')
        if data['last_name'] == "":
            errors.append('last name cannot be blank')
        elif len(data['last_name']) < 2:
            errors.append('last name cannot be fewer than 2 characters')
        if not data['last_name'].isalpha():
            errors.append('last name must only be characters')
        if not EMAIL_REGEX.match(data['email']):
            errors.append('email must be a valid format')
        if data['password'] < 8:
            errors.append('password must be atleast 8 characters')
        if data['password'] != data['confirm_password']:
            errors.append('passwords must match')
        try:
            Users.objects.get(email=data['email'])
            errors.append('email is already in use')
        except:
            pass

        if len(errors) == 0:
            hashed = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
            user = Users.objects.create(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], password=hashed, confirm_password=data['confirm_password'])
            return {'users': user, 'errors': None}
        else:
            return{'users': None, 'errors': errors}

    def login(self, data):
        errors=[]
        messages=[]

        if Users.objects.filter(email = data['email']):
            hashed = Users.objects.get(email = data['email']).password.encode()
            password = data['password'].encode()
            if bcrypt.hashpw(password, hashed) == hashed:
                messages.append("Success!")
            else:
                errors.append('incorrect login/password')
        else:
            errors.append('incorrect login/password')

        if len(errors) == 0:
            user = Users.objects.get(email=data['email'])
            return {'users': user, 'errors': None}
        else:
            return{'users': None, 'errors': errors}

class PostsManager(models.Manager):
    def post(self,data):
        Posts.objects.create(post=data['posts'], user_id=data['id'])

class LikesManager(models.Manager):
    def like(self,data):
        Likes.objects.create(like=True, post_id=data['post_id'], user_id=data['user_id'])

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UsersManager()

class Posts(models.Model):
    post = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(Users, related_name='secrets_created')
    objects = PostsManager()

class Likes(models.Model):
    like = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(Users, related_name='user_likes')
    post_id = models.ForeignKey(Posts, related_name='secret_likes')
    objects = LikesManager()
