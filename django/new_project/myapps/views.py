from django.shortcuts import render


# Create your views here.
def Index(request):
    return render(request,"myapps/Index.html")
def About(request):
    return render(request,"myapps/About.html")
def Contact(request):
    return render(request,"myapps/Contact.html")