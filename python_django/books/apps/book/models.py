from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now=True)
    in_print = models.BooleanField()
