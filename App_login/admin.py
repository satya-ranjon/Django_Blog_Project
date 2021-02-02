from App_login.forms import registion
from django.contrib import admin
from .models import UserProfile,UserProfileBackround
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserProfileBackround)