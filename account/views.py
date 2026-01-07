from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate

from .forms import RegisterForm, LoginForm


class Register(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home")
        form = RegisterForm
        return render(request, "account/register.html", {"form": form})
    
    def post(self, request):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        return redirect("register")


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home")
        form = LoginForm
        return render(request, "account/login.html", {"form": form})
    
    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user:
                login(request, user)
                return redirect("home")
        return redirect("login")
            


            
