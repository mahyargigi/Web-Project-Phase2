from django.db import models
from accounts.models import UserProfile
from content.models import Movie

from datetime import datetime

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(UserProfile)
    movie = models.ForeignKey(Movie)
    rate = models.IntegerField()
    description = models.CharField(max_length=10000)
    date = models.DateTimeField(default=datetime.now())


class Comment(models.Model):
    user = models.ForeignKey(UserProfile)
    post = models.ForeignKey(Post)
    description = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now())


class Like(models.Model):
    user = models.ForeignKey(UserProfile)
    post = models.ForeignKey(Post)
    date = models.DateTimeField(default=datetime.now())


class Notification(models.Model):
    pass