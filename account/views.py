from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login

from .forms import RegisterForm


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

            
