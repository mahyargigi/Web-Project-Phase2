from django.shortcuts import render
from django.http import HttpResponse
from content.models import Artist, Movie, Role
from accounts.models import UserProfile
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import random
# Create your views here.


@login_required
def movie_profile(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    role = Role.objects.filter(movie=movie)
    suggestedFilms = suggested_films(request)
    suggestedUsers = suggested_users(request)
    return render(request,'movie-profile.html',{'movie':movie , 'roles':role , 'suggested_movies':suggestedFilms , 'suggested_users':suggestedUsers})


@login_required
def suggested_films(request):
    movie_list = random.sample(range(0,Movie.objects.count()),2)
    movies = []
    movies.append(Movie.objects.all()[movie_list[0]])
    movies.append(Movie.objects.all()[movie_list[1]])
    #return render(request , 'suggested-films.html' , {'movies':movies})
    return movies


@login_required
def suggested_users(request):
    followings = request.user.user.follows.all().values('id')
    print(followings)
    not_followed_users = UserProfile.objects.exclude(id__in=followings)
    users = []
    if not_followed_users.count() >= 2:
        user_list = random.sample(range(0,not_followed_users.count()),2)
        users.append(not_followed_users[user_list[0]])
        users.append(not_followed_users[user_list[1]])
    elif not_followed_users.count() == 1:
        users.append(not_followed_users[0])
    return users


@login_required
@csrf_exempt
def search(request):
    if request.method == 'POST':
        #print("post")
        query = request.POST.get('query')
        #query = request.POST.get('search')
        #print(query)
        movies = Movie.objects.filter(title__contains=query)
        users = UserProfile.objects.filter(display_name__contains=query)
        #suggestFilms = suggested_films(request)
        #suggestedUsers = suggested_users(request)
        response = render(request, 'search-result.html',{'movies':movies , 'users':users } )
        return HttpResponse(response)
    elif request.method =='GET':
        print("get")
        movies = []
        users = []
        return render(request, 'search.html', {'movies':movies , 'users':users} )
    pass



