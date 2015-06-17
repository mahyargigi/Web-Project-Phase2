from django.shortcuts import render
from .models import Post
# Create your views here.
def post(request , post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comments
    return render(request , 'post.html' , {'post':post})