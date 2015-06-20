from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from accounts.models import UserProfile
from json import dump
from django.views.decorators.csrf import csrf_exempt
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
    if request.method=='Post':
        response = {}
        return HttpResponse(dump(response), content_type="application/json");
    return HttpResponse('');