from django.views.static import serve
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounds/', include('App_login.urls')),
    path('post/', include('App_post.urls')),
    path('',views.home, name='home'),
]

handler404 = views.handler404
handler400 = views.handler404

urlpatterns +=  staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)