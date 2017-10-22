from __future__ import unicode_literals

from django.db import models
from django.db import migrations, models


class Users(models.Model):
    username = models.CharField(max_length = 255)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

class Requests(models.Model):
    itemName= models.CharField(max_length = 255)
    category = models.CharField(max_length=255)
    requestorInfo = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

class Donations(models.Model):
    item = models.CharField(max_length = 255)
    category = models.CharField(max_length = 255)
    donorInfo = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

