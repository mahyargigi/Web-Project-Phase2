from django.contrib.auth import authenticate
from django.contrib import auth
from django.shortcuts import render
from accounts.forms import UserProfileForm, UserForm, LoginForm, UserProfileEditForm, UserEditForm
from accounts.models import UserProfile
from django.http.response import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


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
                    return HttpResponseRedirect("/signup/")
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
            return HttpResponseRedirect('/login/')

    else:
        print("not post", request.GET)

    return render(request, 'user_profile_update_form.html', {'form1': form1, 'form2': form2})

