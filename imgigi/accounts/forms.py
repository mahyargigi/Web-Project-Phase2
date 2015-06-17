# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
#  from captcha.fields import ReCaptchaField
from django import forms
from accounts.models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput()
    )
    password_confirm = forms.CharField(
        label="Password Repeat",
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = {'username', 'first_name', 'last_name', 'password', 'password_confirm'}

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Password don't math")
        return password_confirm

    def save(self, *args, **kwargs):
        kwargs['commit'] = False
        user = super(UserForm, self).save(*args, **kwargs)
        user.set_password(self.cleaned_data.get("password"))
        user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})


class UserProfileForm(forms.ModelForm):
    #captcha = ReCaptchaField(attrs={'theme': 'clean'})

    class Meta:
        model = UserProfile
        exclude = {'user'}

