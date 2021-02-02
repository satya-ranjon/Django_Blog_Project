import django
from django.contrib.messages.api import success
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from .forms import registion,User_login,UserChangeProInfo,add_profilePic,BackgroundImage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .models import UserProfile

# Create your views here.


def retistion(request):
    form = registion()
    if request.method == 'POST':
        form = registion(data = request.POST)
        if form.is_valid():
           form.save()
           messages.success(request,'You have Successfully Sign up here ! Please @Login')
           return HttpResponseRedirect(reverse('App_login:login'))
    return render(request,'App_login/registion.html',context={'form':form})

def login_user(request):
    form = User_login()
    if request.method == 'POST':
        form = User_login(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data .get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login (request,user)
                messages.success(request,'You have successfully Login')
                return HttpResponseRedirect(reverse('home'))
    return render(request,'App_login/login.html', context={'form':form })

@login_required()
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_login:profile_info'))

@login_required()
def ChangeProInfo(request):
    form = UserChangeProInfo(instance=request.user)
    if request.method == 'POST':
        form = UserChangeProInfo(request.POST,instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Your information successfully Update !')
            return HttpResponseRedirect(reverse('App_login:profile_info'))
    return render(request,'App_login/ch_pro_info.html',context={'form':form})

@login_required()
def password_change(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Password Successfully Change !')
            return HttpResponseRedirect(reverse('App_login:profile_info'))
    return render(request,'App_login/password_ch.html',context={'form':form})


# Profile Image
@login_required()
def ProfilePicAdd(request):
    form = add_profilePic()
    if request.method =='POST':
        form = add_profilePic(request.POST,request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            messages.success(request,'Your Profile Picture Successfully Add ')
            return HttpResponseRedirect(reverse('App_login:profile_info'))
    return render(request,'App_login/profile.html',context={'form':form})

@login_required()
def change_pro_pic(request):
    form = add_profilePic(instance=request.user.user_profile)
    if request.method == 'POST':
        form = add_profilePic(request.POST,request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Profile Picture Successfully Add ')
            return HttpResponseRedirect(reverse('App_login:profile_info'))
    return render(request,'App_login/profile_pic_ch.html',context={'form':form})


# Profile BackgroundImage
@login_required()
def bag_img_profile(request):
    form = BackgroundImage()
    if request.method =='POST':
        form = BackgroundImage(request.POST,request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            messages.success(request,'Your Profile Picture Successfully Add ')
            return HttpResponseRedirect(reverse('App_login:profile_info'))
    return render(request,'App_login/background.html',context={'form':form})

@login_required()
def change_pro_pic_bg(request):
    form = BackgroundImage(instance=request.user.user_profile_bg)
    if request.method == 'POST':
        form = BackgroundImage(request.POST,request.FILES, instance=request.user.user_profile_bg)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Profile Picture Successfully Add ')
            return HttpResponseRedirect(reverse('App_login:profile_info'))
    return render(request,'App_login/background.html',context={'form':form})


