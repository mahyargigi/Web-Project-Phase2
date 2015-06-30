from django.shortcuts import render
from .models import Post, Comment
from django.http import HttpResponse
from accounts.models import UserProfile
from posts.models import Like
from json import dump
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
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
        Comment(user = request.user.user , post = Post.objects.get(id=post_id) , description = comment , date = datetime.now()).save()
        comment_list = Comment.objects.filter(post = Post.objects.get(id = post_id))
        #return HttpResponse('')
        response = render(request, 'comments.html', {'comments':comment_list})
        return HttpResponse(response)

        #return HttpResponse(json.dump(comment_list), mimetype="application/json")

@csrf_exempt
def like(request):
    if request.method == 'POST':
        post_id = request.POST.get('id')
        like = Like.objects.filter(post=Post.objects.get(id=post_id) , user=request.user.user )
        if like:
            like.delete()
        else:
            Like(user=request.user.user , post=Post.objects.get(id=post_id) , date = datetime.now()).save()
        likes = Like.objects.filter(post = Post.objects.get(id=post_id))
        response = render(request, 'likes.html', {'likes':likes})
        return HttpResponse(response)
    pass


