from django.shortcuts import render

# Create your views here.
def logins(request):
    return render(request,'login.html')
