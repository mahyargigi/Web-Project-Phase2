# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20150619_1131'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notification',
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 2, 6, 35, 7, 95859, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='like',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 2, 6, 35, 7, 96859, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(to='posts.Post', related_name='likes'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 2, 6, 35, 7, 95859, tzinfo=utc)),
        ),
    ]
