# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('display_name', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('profile_picture', models.ImageField(upload_to='')),
                ('follows', models.ManyToManyField(to='accounts.UserProfile', related_name='followers')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='user')),
            ],
        ),
    ]
