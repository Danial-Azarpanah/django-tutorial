from django.shortcuts import render
from django.views.generic import View

from .models import Info, Message


class Contact(View):
    def get(self, request):
        info = Info.objects.last()
        return render(request, "info/contact.html", {"info": info})
    
    def post(self, request):
        Message.objects.create(
            name=request.POST["name"],
            email=request.POST["email"],
            subject=request.POST["subject"],
            body=request.POST["message"],
        )
        info = Info.objects.last()
        return render(request, "info/contact.html", {"info": info})