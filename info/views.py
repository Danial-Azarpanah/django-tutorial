from django.shortcuts import render, redirect
from django.views.generic import View

from .models import Info, Message
from .forms import ContactForm


class Contact(View):
    def get(self, request):
        info = Info.objects.last()
        return render(request, "info/contact.html", {"info": info, "form": ContactForm})
    
    def post(self, request):
        form = ContactForm(data=request.POST)
        if form.is_valid():
            # Message.objects.create(
            #     name=form.cleaned_data["name"],
            #     email=form.cleaned_data["email"],
            #     subject=form.cleaned_data["subject"],
            #     body=form.cleaned_data["body"],
            # )
            form.save()
        # info = Info.objects.last()
        # return render(request, "info/contact.html", {"info": info, "form": form})
        return redirect("contact")