
from django.conf.urls import include, url
from django.contrib import admin
from bsstest import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/',include(admin.site.urls)),
    url(r'^register/$', views.register,name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^bsstest/$',views.bsstest),
   
]
