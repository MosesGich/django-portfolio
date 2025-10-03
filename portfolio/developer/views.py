from django import forms
from django.shortcuts import render
from django.http import HttpResponse

class NewForm(forms.Form):
    email = forms.EmailField(label="Email")
    message = forms.CharField(label="Optional message")

# Create your views here.
def index(request):
    return render(request, "developer/home.html")

def about(request):
    return render(request,"developer/about.html")

def contact(request):
    if request.method == "POST":
        return HttpResponse("Thankyou")
    return render(request, "developer/contact.html")