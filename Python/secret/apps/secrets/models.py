# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UsersManager(models.Manager):
    def register(self, data):
        fn = data['first_name']
        ln = data['last_name']
        pw = data['password']
        errors=[]

        if fn == "":
            errors.append('first name cannot be blank')
        elif len(fn) < 2:
            errors.append('first name cannot be fewer than 2 characters')
        if not fn.isalpha():
            errors.append('first name must only be characters')
        if ln == "":
            errors.append('last name cannot be blank')
        elif len(ln) < 2:
            errors.append('last name cannot be fewer than 2 characters')
        if not ln.isalpha():
            errors.append('last name must only be characters')
        if not EMAIL_REGEX.match(data['email']):
            errors.append('email must be a valid format')
        elif (data['email']) == "":
            errors.append('email cannot be blank')
        if pw == "":
            errors.append('password cannot be blank')
        elif pw != data['confirm_password']:
            errors.append('passwords must match')

        try:
            Users.objects.get(email=data['email'])
            errors.append('email is already in use')
        except:
            pass

        if len(errors) == 0:
            hashed = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
            user = Users.objects.create(first_name=fn, last_name=ln, email=data['email'], password=hashed, confirm_password=data['confirm_password'])
            return {'users': user, 'errors': None}
        else:
            return{'users': None, 'errors': errors}

    def login(self, data):
        errors = []
        name = None
        userid = None
        Bpw = bcrypt.hashpw(data['pword'].encode(), bcrypt.gensalt())
        print Bpw

        try:
            Users.objects.get(email=data['email'])
        except:
            errors.append('email incorrect')

        if Users.objects.filter(email = data['email']):
           hashed = Users.objects.get(email = data['email']).password.encode()
           password = data['pword'].encode()
           if bcrypt.hashpw(password, hashed) == hashed:
               name = (Users.objects.get(email=data['email']).first_name)
               userid = (Users.objects.get(email=data['email']).id)
               pass
           else:
               errors.append('incorrect login/password')

        if len(errors) == 0:
            return {'errors': None, 'name': name, 'userid': userid}
        else:
            return{'errors': errors}

    def secretPOSTER(self, data):
        if len(data['secret']) > 0:
            oneid = Users.objects.get(id=data['id'])
            print oneid
            Message.objects.create(secret=data['secret'], user_id=oneid)
            return

    def likeCounter(self, data):
        user = Users.objects.get(id=data['userid'])
        message = Message.objects.get(id=data['POSTid'])

        try:
            if Likes.objects.get(message_id=message, user_id=user).like == True:
                pass
        except:
            Likes.objects.create(like = True, message_id=message, user_id=user)

        COUNT = Likes.objects.filter(message_id=data['POSTid'], like = True).count()

        return {'good': True, 'count':COUNT}

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UsersManager()

class Message(models.Model):
    secret = models.TextField()
    user_id = models.ForeignKey(Users, related_name='secrets')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UsersManager()

class Likes(models.Model):
    like = models.BooleanField(default=False)
    user_id = models.ForeignKey(Users, related_name='likes')
    message_id = models.ForeignKey(Message, related_name='messages')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
