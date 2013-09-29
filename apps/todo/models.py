__author__ = 'dumingtan'

from django.db import models

class Item(models.Model):
    id = models.IntegerField()
    type = models.CharField(max_length=10)
    content = models.CharField(max_length=1000)
    time = models.TimeField()

class whoCreate(models.Model):
    user = models.CharField()
    itemId = models.IntegerField()