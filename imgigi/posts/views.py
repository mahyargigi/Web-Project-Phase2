from django.shortcuts import render
from .models import Post
from accounts.models import UserProfile
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