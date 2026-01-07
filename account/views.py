from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout

from .forms import RegisterForm, LoginForm, ProfileForm


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


class Logout(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("home")
        logout(request)
        return redirect("home")


class Profile(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("login")
        form = ProfileForm(instance=request.user)
        return render(request, "account/profile.html", {"form": form})
    
    def post(self, request):
        form = ProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("home")
        print(form.errors)
        return redirect("profile")
            
