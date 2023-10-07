import django.shortcuts
from django.urls import include, path

from . import views


urlpatterns = [
    path("", views.index, name = "index"),
    path("reg", views.Reg.as_view(), name = "reg"),
    path("login", views.Login.as_view(), name = "login"),
    path("logout", views.LogoutView.as_view(), name = "logout"),
    
    path("profile", views.profile, name = "profile"),
    
    
    
]
