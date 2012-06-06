from django.db import models
import datetime
from django.contrib.auth.models import User

class News(models.Model):
    text = models.TextField()
    date = models.DateField(auto_now = datetime.datetime.now(),auto_now_add = datetime.datetime.now())

class DoYouKnowThis(models.Model):
    text = models.TextField()
    date = models.DateField(auto_now = datetime.datetime.now(),auto_now_add = datetime.datetime.now())

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    Rss = models.CharField(max_length = 100)