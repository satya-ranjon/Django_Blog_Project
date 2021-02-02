from django.urls import path
from . import views

app_name= 'App_post'

urlpatterns = [
    path('', views.home, name='home'),
    path('MyBlogs', views.MyBlogs.as_view(), name='MyBlogs'),
    path('EditBlog/<pk>/', views.EditBlog.as_view(), name='EditBlog'),
    path('Create_blog/', views.Create_blog.as_view(), name='Create_blog'),
    # path(r'^BlogDitlis/(?P<slug>[\w-]+)/$',views.blog_deitels,name='blog_detiels'),
    path('BlogDitlis/<slug>/',views.blog_deitels,name='blog_detiels'),
    # path(r'^BlogDitlis1/(?P<slug>[\w-]+)/$',views.BlogDetitel,name='BlogDetitel1'),
    path('BlogDitlis1/<slug>/',views.BlogDetitel,name='BlogDetitel1'),
    path('Like/<pk>/',views.UserLike, name='like'),
    path('unLike/<pk>/',views.UserUnlike, name='Unlike'),
    path('orprofile/<username>/',views.OrderUserProfile, name='or_profile'),

]
