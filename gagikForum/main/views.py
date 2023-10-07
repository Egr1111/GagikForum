from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.views.generic import (
    DetailView,
    UpdateView,
    DeleteView,
    TemplateView,
    ListView,
    CreateView,
    View
)
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required

menu = [
        {"Главная": {"url": "/", "subclass": None}},
        {"Отзывы и предложения": {"url": "/review/", "subclas": None}},
        {
            "Конкурсы": {
                "url": "/contests/",
                "subclass": {
                    "Конкурс ведущих": {
                        "url": "/contests/ved",
                        "subclass": {"Аудио": {"url": "/contests/ved/audio/"}},
                    },
                    "Чтецы. Профессионалы.": {
                        "urls": "/contests/prof/",
                        "subclass": None
                    }
                },
            }
        },
    ]
users = User.objects.all()
# Create your views here.
def index(request):
    return render(request, "main/index.html", {"menu": menu, "users": users})


class Reg(CreateView):
    template_name = "main/enter.html"
    form_class = UserCreateForm
    success_url = reverse_lazy("login")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = menu
        context["users"] = users
        
        return context
    

class Login(LoginView):
    template_name = "main/login.html"
    form_class = UserLoginForm
    success_url = reverse_lazy("index")
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = menu
        context["users"] = users
        
        return context

@login_required
def profile(request):
    error = ""
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = UserForm(instance=request.user)
        
    return render(request, "main/profile.html", {"menu": menu, "users": users, "form": form})


        