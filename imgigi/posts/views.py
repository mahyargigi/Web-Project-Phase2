from django.shortcuts import render
from .models import Post, Comment, Movie
from django.http import HttpResponse
from accounts.models import UserProfile
from posts.models import Like
from json import dump
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from notifications import notify
import django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from content.views import suggested_users, suggested_films


@login_required
def post(request, post_id):
    post = Post.objects.get(id=post_id)
    #comments = post.comments
    print("post-id is: " + post_id)
    suggestedFilms = suggested_films(request)
    suggestedUsers = suggested_users(request)
    return render(request, 'post.html',
                  {'post': post, 'suggested_movies': suggestedFilms, 'suggested_users': suggestedUsers})


@login_required
@csrf_exempt
def timeline(request, page_index=0):
    ppp = 2 #post per page!
    page_index = int(page_index)
    first = page_index * ppp
    last = (page_index + 1) * ppp
    #print(page_index)
    user = request.user.user
    followings_id = user.follows.all().values('id')
    last_posts = Post.objects.filter(user__in=followings_id).order_by('date').reverse()
    suggestedFilms = suggested_films(request)
    suggestedUsers = suggested_users(request)
    if page_index == 0:
        last_posts = last_posts[first:last]
        return render(request, 'timeline.html',
                      {'posts': last_posts, 'suggested_movies': suggestedFilms, 'suggested_users': suggestedUsers})
    else:
        if first > last_posts.count():
            return HttpResponse("End of timeline")
        if last > last_posts.count():
            last_posts = last_posts[first]
        else:
            last_posts = last_posts[first:last]

        print("last"+str(last_posts[0]))
        return render(request, 'infinite-scroll-posts.html',
                      {'posts': last_posts})


@login_required
@csrf_exempt
def post_comment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
        Comment(user=request.user.user, post=post, description=comment, date=django.utils.timezone.now()).save()
        notify.send(request.user.user, recipient=post.user.user,
                    verb=str(request.user) + " commented on your post") #notification baraye sahebe user
        user_id_vals = Comment.objects.filter(post_id=post.id).values('user')
        recipients = User.objects.filter(user__in=user_id_vals).exclude(user__in=[post.user, request.user.user])
        print(recipients)
        for rec in recipients:
            notify.send(request.user.user, recipient=rec, verb="commented on " + str(post.user.display_name) + "'s post")

        comment_list = Comment.objects.filter(post=Post.objects.get(id=post_id))
        #return HttpResponse('')
        response = render(request, 'comments.html', {'comments': comment_list})
        return HttpResponse(response)

        #return HttpResponse(json.dump(comment_list), mimetype="application/json")


@login_required
@csrf_exempt
def like(request):
    if request.method == 'POST':
        post_id = request.POST.get('id')
        post = Post.objects.get(id=post_id)
        like = Like.objects.filter(post=post, user=request.user.user)
        if like:
            like.delete()
        else:
            Like(user=request.user.user, post=post, date=django.utils.timezone.now()).save()
            notify.send(request.user.user, recipient=post.user.user, verb=str(request.user) + " liked your post")
        likes = Like.objects.filter(post=post)
        response = render(request, 'likes.html', {'likes': likes})
        return HttpResponse(response)
    pass


@login_required
@csrf_exempt
def red_notifications(request):
    user = request.user
    user.notifications.mark_all_as_read()
    return HttpResponse("success")


@login_required
@csrf_exempt
def add_post(request):
    if request.method == "POST":
        user_rate = int(request.POST.get('user_rate'))
        #print("user rate is :"+str(user_rate))
        user_description = request.POST.get('user_description')
        #print("user description is"+str(user_description))
        movie_id = request.POST.get('movie_id')
        #print("movie id is "+str(movie_id))
        movie = Movie.objects.get(id=movie_id)
        #print(movie.title)
        Post(user=request.user.user, movie=movie, rate=int(user_rate), description=str(user_description)).save()
        rate_weight = int(movie.rate_weight)
        new_movie_rating = (((rate_weight * movie.rating) + (user_rate)) / (rate_weight + 1))
        movie.rating = new_movie_rating
        movie.rate_weight = rate_weight + 1
        movie.save()
        return HttpResponse(new_movie_rating)