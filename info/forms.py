from django import forms
from django.core.exceptions import ValidationError

from .models import Message


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "Your name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Your email"}))
    subject = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"placeholder": "Subject"}))
    body = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Your message"}))

    def clean_name(self):
        name = self.cleaned_data["name"]
        if name == "admin":
            raise ValidationError("نام نمی‌تواند ادمین باشد")
        return name
    
    def clean(self):
        subject = self.cleaned_data["subject"]
        body = self.cleaned_data["body"]
        if subject == body:
            raise ValidationError("موضوع و بدنه نمی‌توانند یکسان باشند")


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ["created_at"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Your email"}),
            "subject": forms.TextInput(attrs={"placeholder": "Subject"}),
            "body": forms.Textarea(attrs={"placeholder": "Your message"}),
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "admin":
            raise ValidationError("نام نمی‌تواند ادمین باشد")
        return name

    def clean(self):
        cleaned_data = super().clean()
        subject = cleaned_data.get("subject")
        body = cleaned_data.get("body")

        if subject and body and subject == body:
            raise ValidationError("موضوع و بدنه نمی‌توانند یکسان باشند")
