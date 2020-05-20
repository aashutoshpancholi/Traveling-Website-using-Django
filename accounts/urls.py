from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
    url("register", views.register, name="register"),
    url("login",views.login, name="login"),
    url("logout",views.logout,name="logout"),

    ]