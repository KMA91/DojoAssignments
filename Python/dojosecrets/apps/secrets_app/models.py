from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import bcrypt
import re
import datetime


EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validateReg(self, userInfo):
        errors = []
        if not userInfo['fname'].isalpha():
            errors.append('First name contains non-alpha character(s)')
        if len(userInfo['fname']) < 2:
            messages.warning(request, 'First name too short.')
        if not userInfo['lname'].isalpha():
            errors.append('Last name contains non-alpha character(s)')
        if len(userInfo['lname']) < 2:
            errors.append('Last name too short.')
        if not EMAIL_REGEX.match(userInfo['em']):
            errors.append('Email is not a valid email!')
        try:
            User.objects.get(email=userInfo['em'])
            errors.append("Email is already registered.")
        except:
            pass
        if len(userInfo['pw']) < 8:
            errors.append('Password is not long enough.')
        if userInfo['pw'] != userInfo['conf_pw']:
            errors.append('Passwords do not match.')

        if userInfo['dob'] == '':
			errors.append("Birthday is required.")
        elif datetime.datetime.strptime(userInfo['dob'], '%Y-%m-%d') >= datetime.datetime.now():
			errors.append("Birthday may not be in the future!!")

        if len(errors) == 0:
            userInfo['pw'] = bcrypt.hashpw(userInfo['pw'].encode('utf-8'), bcrypt.gensalt())
            new_user = User.objects.create(first_name = userInfo['fname'], last_name = userInfo['lname'], email = userInfo['em'], password = userInfo['pw'], birthday= userInfo['dob'])
            return {
            'new': new_user,
            'error_list': None
            }
        else:
            return {
            'new': None,
            'error_list': errors
            }

    def userLogin(self, log_data):
        errors=[]
        try:
			found_user = User.objects.get(email=log_data['loginEmail'])
			if bcrypt.hashpw(log_data['loginPw'].encode('utf-8'), found_user.password.encode('utf-8')) != found_user.password.encode('utf-8'):
				errors.append("Incorrect password.")
        except:
			#email does not exist in the database
			errors.append("Email address not registered.")
        if len(errors)==0:
            return {
                'logged_user': found_user,
                'list_errors': None
            }
        else:
            return {
                'logged_user': None,
                'list_errors': errors
            }

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class SecretManager(models.Manager):
    def add_secret(self, secretInfo):
        if len(secretInfo['secretmsg']) == 0:
            pass
        else:
            secretid = User.objects.get(id=secretInfo['secretuser'])
            new_secret = Secret.objects.create(user_id=secretid, secret=secretInfo['secretmsg'])
            return {
                'n_secret': new_secret
            }
    def delete_secret(self, secretInfo):
        del_secret = Secret.objects.get(id=secretInfo['secretid']).delete()
        return {
        'd_secret': del_secret
        }

    def like_secret(self, likeInfo):
        userlike = User.objects.get(id=likeInfo['secretuser'])
        likeuser = Secret.objects.get(id=likeInfo['secretid'])
        like_s = likeuser.likes.add(userlike)
        print userlike
        print likeuser
        print like_s
        return {
        'l_secret': like_s
        }


class Secret(models.Model):
    user_id = models.ForeignKey(User, related_name="secrets")
    secret = models.TextField(max_length=1000)
    likes = models.ManyToManyField(User, related_name="secrets_like")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = SecretManager()
