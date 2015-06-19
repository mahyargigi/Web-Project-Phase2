from django.shortcuts import render
from django.http import HttpResponse
from content.models import Artist, Movie, Role
from accounts.models import UserProfile
from random import randint
import random
# Create your views here.

def movie_profile(request, movie_id):

    #try :
    movie = Movie.objects.get(id=movie_id)
    role = Role.objects.filter(movie=movie)
    return render(request,'movie-profile.html',{'movie':movie , 'roles':role})

    #except:
    #    return HttpResponse('not found')

def suggested_films(request):
    movie_list = random.sample(range(0,Movie.objects.count()),2)
    movies = []
    movies.append(Movie.objects.all()[movie_list[0]])
    movies.append(Movie.objects.all()[movie_list[1]])
    return render(request , 'suggested-films.html' , {'movies':movies})

def search_movie(request , query):

    pass



