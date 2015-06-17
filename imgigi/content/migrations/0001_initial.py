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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=10000)),
                ('length', models.IntegerField()),
                ('imdb_link', models.URLField()),
                ('release_date', models.DateField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2, default=0)),
                ('movie_cover', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('role', models.CharField(choices=[('dir', 'Director'), ('crt', 'Creator/Writer'), ('act', 'Actor')], max_length=3)),
                ('description', models.CharField(blank=True, null=True, max_length=1000)),
                ('artist', models.ForeignKey(to='content.Artist')),
                ('movie', models.ForeignKey(to='content.Movie')),
            ],
        ),
    ]
