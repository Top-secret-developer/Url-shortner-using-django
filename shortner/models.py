from django.db import models

# Create your models here.
class Url(models.Model):
    Link =  models.CharField(max_length=10000)
    uuid = models.CharField(max_length=77)
