from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, related_name='user')
    display_name = models.CharField(max_length=100, null=False, blank=False)
    birthday = models.DateField(null=False, blank=False)
    profile_picture = models.ImageField()
    follows = models.ManyToManyField('self', related_name='followers', symmetrical=False)
