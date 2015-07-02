from django.shortcuts import render
from .models import Post, Comment , Movie
from django.http import HttpResponse
from accounts.models import UserProfile
from posts.models import Like
from json import dump
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from notifications import notify
import django
from django.contrib.auth.models import User
import json
# Create your views here.
def post(request , post_id):
    post = Post.objects.get(id=post_id)
    #comments = post.comments
    print("post-id is: "+post_id)
    return render(request , 'post.html' , {'post':post})

def timeline(request):
    user = UserProfile.objects.get(id=2)
    followings = []
    for following in user.follows.all():
        followings.append(following)
    posts = []
    for following in followings:
        for post in following.posts.all():
            posts.append(post)
    #posts = sorted(posts, key=attrgetter('posts.date'))
    posts.sort(key=lambda r: post.date) #az old be new sort mikone
    posts.reverse() # barax mikonim liste sort shode ro
    #posts.order_by('date')
    return render(request,'timeline.html', {'posts': posts})
    #pass


@csrf_exempt
def post_comment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
        Comment(user = request.user.user , post =post  , description = comment , date = datetime.now()).save()
        notify.send(request.user, recipient=post.user.user , verb=str(request.user)+" commented on your post" ) #notification baraye sahebe user
        user_id_vals = Comment.objects.filter(post_id=post.id).values('user')
        recipients = User.objects.filter(user__in=user_id_vals).exclude(user__in=[post.user,request.user.user])
        print(recipients)
        for rec in recipients:
            notify.send(request.user, recipient=rec , verb="commented on "+str(post.user.display_name)+"'s post" )


        comment_list = Comment.objects.filter(post = Post.objects.get(id = post_id))
        #return HttpResponse('')
        response = render(request, 'comments.html', {'comments':comment_list})
        return HttpResponse(response)

        #return HttpResponse(json.dump(comment_list), mimetype="application/json")

@csrf_exempt
def like(request):
    if request.method == 'POST':
        post_id = request.POST.get('id')
        post = Post.objects.get(id=post_id)
        like = Like.objects.filter(post=post , user=request.user.user )
        if like:
            like.delete()
        else:
            Like(user=request.user.user , post=post , date = django.utils.timezone.now()).save()
            notify.send(request.user, recipient=post.user.user , verb=str(request.user)+" liked your post")
        likes = Like.objects.filter(post = post)
        response = render(request, 'likes.html', {'likes':likes})
        return HttpResponse(response)
    pass

@csrf_exempt
def red_notifications(request):
    user = request.user
    user.notifications.mark_all_as_read()
    return HttpResponse("success")

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
        Post(user=request.user.user , movie=movie ,rate=int(user_rate),description=str(user_description)).save()
        rate_weight = int(movie.rate_weight)
        new_movie_rating = (((rate_weight * movie.rating)+(user_rate))/(rate_weight+1))
        movie.rating = new_movie_rating
        movie.rate_weight = rate_weight + 1
        movie.save()
        return HttpResponse(new_movie_rating)