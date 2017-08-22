# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import re
import bcrypt

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

        if data['password'] != data['confirm_password']:
            errors.append('passwords must match')

        try:
            Users.objects.get(email=data['email'])
            errors.append('email is already in use')
        except:
            pass
        if len(errors) == 0:
            Bpw = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
            user = Users.objects.create(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], password=Bpw, confirm_password=data['confirm_password'])
            return {'users': user, 'errors': None}
        else:
            return{'users': None, 'errors': errors}

    def login(self, data):
        errors = []
        try:
            user = user.objects.get(email=data['email'])
            if bcrypt.hashpw(data['pw'], user.password) == user.password
            print 'GOOD!'
        except:
            errors.append('email and/or password incorrect')

        if len(errors) == 0:
            return {'errors': None}
        else:
            return{'errors': errors}

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UsersManager()
