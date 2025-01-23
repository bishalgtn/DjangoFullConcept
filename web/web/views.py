from django.http import HttpResponse

def homePage(request):
    return HttpResponse("Hi, this is home page of the app")

def aboutPage(request):
    return HttpResponse("This is about page")