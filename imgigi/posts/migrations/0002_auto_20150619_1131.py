# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 19, 7, 1, 5, 731407, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='posts.Post', related_name='comments'),
        ),
        migrations.AlterField(
            model_name='like',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 19, 7, 1, 5, 731407, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 19, 7, 1, 5, 730406, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(to='accounts.UserProfile', related_name='posts'),
        ),
    ]
