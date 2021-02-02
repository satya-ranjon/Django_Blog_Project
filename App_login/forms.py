from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField
from django.forms import fields
from django.forms.widgets import Widget
from .models import UserProfile,UserProfileBackround


class registion (UserCreationForm):
    email = forms.EmailField(required=True, label='', widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1 = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder':' Password', 'type':'password'}))
    password2 = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder':' Password Confarmition', 'type':'password'}))
    class Meta:
        model = User
        fields =('email','username','password1','password2',)

class User_login(AuthenticationForm):
    username = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder':' Password', 'type':'password'}))
    class Meta:
        fields = ('username','password')

class UserChangeProInfo(UserChangeForm):
    email = forms.EmailField(required=False, label='', widget=forms.TextInput(attrs={'placeholder':' Email'}))
    username = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder':' Username'}))
    first_name = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder':'first_name'}))
    last_name = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder':' last_name'}))
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')


class add_profilePic(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic',)

class BackgroundImage(forms.ModelForm):
    class Meta:
        model = UserProfileBackround
        fields = ('profile_pic_bg',)


# class PasswordChUser(PasswordChangeForm):
#     password = forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':' Carrent Password','type':'password'}))
#     password1 = forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':' New Password','type':'password'}))
#     password2 = forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':' Conform Password','type':'password'}))
#     class Meta:
#         fields = ('password','password1','password2',)