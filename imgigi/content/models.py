from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)
    length = models.IntegerField()
    imdb_link = models.URLField()
    release_date = models.DateField()
    rating = models.DecimalField()  # aggregate this! or change on every post!
    movie_cover = models.ImageField()


class Artist(models.Model):
    name = models.CharField(max_length=1000, null=False, blank=False)


class Role(models.Model):
    movie = models.ForeignKey(model=Movie)
    artist = models.ForeignKey(model=Artist)
    ROLE_CHOICES = (
        ('dir', 'Director'),
        ('crt', 'Creator/Writer'),
        ('act', 'Actor'),
    )
    role = models.CharField(choices=ROLE_CHOICES, max_length=3)
    # for Actors and Casts:
    description = models.CharField(max_length=1000, null=True, blank=True)


    # class Genre(models.Model):
    # pass