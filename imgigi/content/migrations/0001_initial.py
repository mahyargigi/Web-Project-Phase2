# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=10000)),
                ('length', models.IntegerField()),
                ('imdb_link', models.URLField()),
                ('release_date', models.DateField()),
                ('rating', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('movie_cover', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('role', models.CharField(max_length=3, choices=[('dir', 'Director'), ('crt', 'Creator/Writer'), ('act', 'Actor')])),
                ('description', models.CharField(null=True, max_length=1000, blank=True)),
                ('artist', models.ForeignKey(to='content.Artist')),
                ('movie', models.ForeignKey(to='content.Movie')),
            ],
        ),
    ]
