#from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
#    return HttpResponse("Hi, this is home page of the app")
    return render(request, 'home.html')

def aboutPage(request):
#    return HttpResponse("This is about page")
    return render(request,'about.html')