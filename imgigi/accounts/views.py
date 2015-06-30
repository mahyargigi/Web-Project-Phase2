from django.shortcuts import render
from .models import UserProfile
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# Create your views here.

def user_profile(request , user_id):
    user = UserProfile.objects.get(id=user_id)
    yours , follows = False , False
    if request.user.user == user :
        yours = True
    elif user in request.user.user.follows.all():
        follows = True
    return render(request , 'user-profile-yours.html' , {'user':user , 'yours':yours , 'follows':follows})

@csrf_exempt
def follow_unfollow(request):
    subject_user = request.user.user
    object_user = UserProfile.objects.get(id = request.POST.get('id'))
    action = ""
    if request.POST.get('action') == 'follow':
        print('11')
        action = "follow"
    elif request.POST.get('action') == 'unfollow':
        print('22')
        action = "unfollow"
    if action == "follow":
        print('33')
        if not object_user in subject_user.follows.all():
            print('44')
            subject_user.follows.add(object_user)
    elif action == "unfollow":
        print('55')
        if object_user in subject_user.follows.all():
            print('66')
            subject_user.follows.remove(object_user)
    return HttpResponse('done!')