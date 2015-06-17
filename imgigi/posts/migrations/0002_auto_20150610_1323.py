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
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 10, 13, 23, 55, 415343, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='like',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 10, 13, 23, 55, 416179, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 10, 13, 23, 55, 414066, tzinfo=utc)),
        ),
    ]
