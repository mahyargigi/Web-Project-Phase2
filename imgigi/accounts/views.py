from django.contrib.auth import authenticate
from django.contrib import auth
from django.shortcuts import render
from accounts.forms import UserProfileForm, UserForm, LoginForm, UserProfileEditForm, UserEditForm
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from notifications import notify
from content.views import suggested_users , suggested_films
# Create your views here.

@login_required
def user_profile(request , user_id=None):
    yours , follows = False , False
    if not user_id:
        yours = True
        user = request.user.user
    else:
        user = UserProfile.objects.get(id=user_id)
        if user in request.user.user.follows.all():
            follows = True
    suggestedFilms = suggested_films(request)
    suggestedUsers = suggested_users(request)
    return render(request , 'user-profile-yours.html' , {'target_user':user , 'yours':yours , 'follows':follows ,'suggested_movies':suggestedFilms , 'suggested_users':suggestedUsers})


@login_required
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
            notify.send(request.user.user, recipient=object_user.user , verb=str(request.user)+" followed you")
    elif action == "unfollow":
        if object_user in subject_user.follows.all():
            subject_user.follows.remove(object_user)
    return HttpResponse('done!')


def signup(request):
    print("in sign up")
    if request.method == 'POST':
        form1 = UserForm(request.POST)
        form2 = UserProfileForm(request.POST)
        print(form1)
        print(form2)
        if form1.is_valid() and form2.is_valid():
            print("valid")
            new_user = form1.save()
            profile = form2.save(commit=False)
            profile.user = new_user
            profile.save()
            return HttpResponseRedirect('/login/')

    else:
        print("not post", request.GET)
        form1 = UserForm()
        form2 = UserProfileForm()

    return render(request, 'signup.html', {'form1': form1, 'form2': form2})


def login(request):
    # TODO: login with oauth google , ...
    # if provider_name != "":
    #     print(provider_name)
    #     response = HttpResponse()
    #     result = authomatic.login(DjangoAdapter(request, response), provider_name)
    #     if result:
    #         print "result is not None"
    #         return HttpResponseRedirect('/time/')
    #     print "nonono"
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    print("OK")
                    return HttpResponseRedirect("/")
                    # return redirected page
                else:
                    return HttpResponse('disabled account')
            else:
                message = 'incorrect pass or not registered'
        else:
            message = 'form is invalid'
    else:
        form = LoginForm()
        message = 'try again'
    return render(request, 'login.html', {'form': form, 'message': message})


@login_required
def edit_user_profile(request):
    instance = request.user
    form1 = UserEditForm(request.POST or None, instance=instance)
    form2 = UserProfileEditForm(request.POST or None, request.FILES or None, instance=(instance.user or None))
    print("in edit profile")
    if request.method == 'POST':
        # form1 = UserForm(request.POST)
        # form2 = UserProfileForm(request.POST)
        # print(form1)
        print(form2)
        if form1.is_valid() and form2.is_valid():
            print("valid")
            u1 = form1.save(commit=False)
            up = form2.save(commit=False)
            instance = u1
            instance.user = up
            instance.save()
            instance.user.save()
            return HttpResponseRedirect('/users/'+str(request.user.user.id))

    else:
        print("not post", request.GET)

    return render(request, 'user_profile_update_form.html', {'form1': form1, 'form2': form2})

