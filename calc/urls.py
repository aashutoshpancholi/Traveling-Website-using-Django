from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^add', views.add, name='add'),
    #url(r'^admin/', admin.site.urls),
    #url(r'^admin/$' , views.home , name='home'),
]