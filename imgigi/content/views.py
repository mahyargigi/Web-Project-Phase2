from django.shortcuts import render
from django.http import HttpResponse
from content.models import Artist, Movie, Role
# Create your views here.

def movie_profile(request, movie_id):

    #try :
    movie = Movie.objects.get(id=movie_id)
    role = Role.objects.filter(movie=movie)
    return render(request,'movie-profile.html',{'movie':movie , 'role':role})

    #except:
    #    return HttpResponse('not found')



