from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    weight = models.IntegerField()
    price = models.IntegerField()
    cost = models.IntegerField()
    category = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now=True)
    modified_on = models.DateTimeField(auto_now=True)
