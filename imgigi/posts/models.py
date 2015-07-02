from django.db import models
from accounts.models import UserProfile
from content.models import Movie

from django.utils import timezone

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(UserProfile , related_name="posts")
    movie = models.ForeignKey(Movie)
    rate = models.IntegerField()
    description = models.CharField(max_length=10000)
    date = models.DateTimeField(default=timezone.now())
    def __str__(self):
        name = str(self.movie) + "--" + str(self.user)
        return name


class Comment(models.Model):
    user = models.ForeignKey(UserProfile)
    post = models.ForeignKey(Post, related_name="comments")
    description = models.CharField(max_length=1000)
    date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        comment = str(self.user)+" said:" + str(self.description[0:10])
        return (comment)


class Like(models.Model):
    user = models.ForeignKey(UserProfile)
    post = models.ForeignKey(Post, related_name="likes")
    date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        like = str(self.user)+" liked "+str(self.post.movie)
        return like


#class Notification(models.Model):
#    pass