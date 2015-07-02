from django.contrib.auth.models import User
from django.db import models
import os
from django.conf import settings
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user')
    display_name = models.CharField(max_length=100, null=False, blank=False)
    birthday = models.DateField(null=False, blank=False)
    profile_picture = models.ImageField(upload_to='static/profile_images', default=os.path.join(settings.STATIC_URL, 'img','bomb.jpg'), null=True, blank=True)
    follows = models.ManyToManyField('self', related_name='followers', symmetrical=False, null=True, blank=True)

    def __str__(self):
        return self.display_name
