from django.db import models

# Create your models here.

class Song(models.Model):
    namesong = models.TextField(max_length=50)
    singer1 = models.TextField(max_length=30)
    singer2 = models.TextField(max_length=30)
    singer3 = models.TextField(max_length=30)
    typeSong = models.TextField(max_length=30)
    week1 = models.DateField(max_length=30)
    week2 = models.DateField(max_length=30)
    picture = models.ImageField(upload_to="imagebd/",null=True, blank=True)

class Singer(models.Model):
    name = models.TextField(max_length=50)
    country = models.TextField(max_length=10)
    photo = models.ImageField(upload_to="imagebd/",null=True, blank=True)
    flag = models.ImageField(upload_to="imagebd/",null=True, blank=True)
    points = models.IntegerField(max_length=10000000)
    awards = models.IntegerField(max_length=10000000)
    position = models.IntegerField(null=True,blank=True)
