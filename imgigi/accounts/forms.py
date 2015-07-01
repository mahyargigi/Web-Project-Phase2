# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
#  from captcha.fields import ReCaptchaField
from django import forms
from accounts.models import UserProfile
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})


class UserForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput()
    )
    password_confirm = forms.CharField(
        label="Password Repeat",
        widget=forms.PasswordInput()
    )
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = {'username', 'password', 'password_confirm', 'email'}

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
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['captcha'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['password_confirm'].widget.attrs.update({'class': 'form-control'})


class UserProfileForm(forms.ModelForm):
    #captcha = ReCaptchaField(attrs={'theme': 'clean'})

    class Meta:
        model = UserProfile
        fields = {'birthday', 'display_name'}

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['birthday'].widget.attrs.update({'class': 'form-control'})
        self.fields['display_name'].widget.attrs.update({'class': 'form-control'})


class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = {'birthday', 'display_name', 'profile_picture'}

    def __init__(self, *args, **kwargs):
        super(UserProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['birthday'].widget.attrs.update({'class': 'form-control'})
        self.fields['display_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['profile_picture'].widget.attrs.update({'class': 'form-control'})


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = {'username', 'email'}

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
