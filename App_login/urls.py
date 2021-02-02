from django.urls import path
from . import views

app_name = 'App_login'

urlpatterns = [
    path('retistion/',views.retistion, name='retistion'),
    path('login/',views.login_user, name='login'),
    # path('profile/',views.change_pro_pic, name='profile_info'),
    path('profile/',views.ProfilePicAdd, name='profile_info'),
    path('change_pro_pic/',views.change_pro_pic, name='change_pro_pic'),

    path('bag_img_profile/',views.bag_img_profile, name='bag_img_profile'),
    path('change_pro_pic_bg/',views.change_pro_pic_bg, name='change_pro_pic_bg'),
    
    path('password_change/',views.password_change, name='password_change'),

    path('logout/',views.logout_user, name='logout'),
    path('ChangeProInfo/',views.ChangeProInfo, name='ChangeProInfo'),
]
