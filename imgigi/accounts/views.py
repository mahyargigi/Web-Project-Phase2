from django.shortcuts import render
from .models import UserProfile
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from notifications import notify
from content.views import suggested_users , suggested_films
# Create your views here.

def user_profile(request , user_id):
    user = UserProfile.objects.get(id=user_id)
    yours , follows = False , False
    if request.user.user == user :
        yours = True
    elif user in request.user.user.follows.all():
        follows = True
    suggestedFilms = suggested_films(request)
    suggestedUsers = suggested_users(request)
    return render(request , 'user-profile-yours.html' , {'target_user':user , 'yours':yours , 'follows':follows ,'suggested_movies':suggestedFilms , 'suggested_users':suggestedUsers})

@csrf_exempt
def follow_unfollow(request):
    subject_user = request.user.user
    print("1")
    object_user = UserProfile.objects.get(id = request.POST.get('id'))
    print("2")
    action = ""
    print("3")
    if request.POST.get('action') == 'follow':
        action = "follow"
    elif request.POST.get('action') == 'unfollow':
        action = "unfollow"
    if action == "follow":
        if not object_user in subject_user.follows.all():
            subject_user.follows.add(object_user)
            notify.send(request.user, recipient=object_user.user , verb=str(request.user)+" followed you")
    elif action == "unfollow":
        if object_user in subject_user.follows.all():
            subject_user.follows.remove(object_user)
    return HttpResponse('done!')

def edit(request):
    #esm-ax-tarikhe tavalod-password
    pass