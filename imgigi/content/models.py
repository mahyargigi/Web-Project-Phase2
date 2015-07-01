from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)
    length = models.IntegerField() #modat zamane film
    imdb_link = models.URLField()
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=2 , decimal_places=1,default=0)  # aggregate this! or change on every post!
    rate_weight = models.IntegerField(default=0)
    movie_cover = models.ImageField(upload_to='movie-covers')

    def __str__(self):
        return self.title

class Artist(models.Model):
    name = models.CharField(max_length=1000, null=False, blank=False)

    def __str__(self):
        return self.name


class Role(models.Model):
    movie = models.ForeignKey(Movie)
    artist = models.ForeignKey(Artist)
    ROLE_CHOICES = (
        ('dir', 'Director'),
        ('crt', 'Creator/Writer'),
        ('act', 'Actor'),
    )
    role = models.CharField(choices=ROLE_CHOICES, max_length=3)
    # for Actors and Casts:
    description = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.artist)+"-"+self.role