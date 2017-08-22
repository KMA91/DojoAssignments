from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def register(self, data):
        errors = []

        print 'HELLOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO'
        if len(data['first']) < 2:
            errors.append('FIRST NAME must not be fewer than 2 characters.')
        if len(data['last']) < 2:
            errors.append('LAST NAME must not be fewer than 2 characters.')
        if not EMAIL_REGEX.match(data['email']):
            errors.append('EMAIL is not in the right format.')
        if len(data['password']) > 8:
            errors.append('PASSWORD must be fewer than 8 characters')
        if data['password'] != data['passwordCON']:
            errors.append('PASSWORD and PASSWORD CONFIRM does not match!')
        try:
            User.objects.get(emailMOD=data['email'])
            errors.append('This email is taken. Use another email.')
        except:
            pass

        if len(errors) == 0:
            user = User.objects.create(f_name=data['first'], l_name=data['last'], emailMOD=data['email'], pwMOD=data['password'])
            return {'user':user, 'errors': None}
        else:
            return {'user':None, 'errors': errors}


class User(models.Model):
    f_name=models.CharField(max_length=255)
    l_name=models.CharField(max_length=255)
    emailMOD=models.EmailField()
    pwMOD=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects = UserManager()
