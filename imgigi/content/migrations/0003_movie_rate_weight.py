# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20150619_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rate_weight',
            field=models.IntegerField(default=0),
        ),
    ]
