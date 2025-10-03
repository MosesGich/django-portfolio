from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "developer/home.html")

def about(request):
    return render(request,"developer/about.html")