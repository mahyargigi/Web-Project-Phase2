from django.shortcuts import render
from accounts.forms import UserProfileForm, UserForm
from django.http.response import HttpResponseRedirect
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form1 = UserForm(request.POST)
        form2 = UserProfileForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            new_user = form1.save()
            profile = form2.save(commit=False)
            profile.user = new_user
            profile.save()
            return HttpResponseRedirect('/accounts/login')

    else:
        form1 = UserForm()
        form2 = UserProfileForm()

    print(form1)

    return render(request, 'signup.html', {'form1': form1, 'form2': form2})
