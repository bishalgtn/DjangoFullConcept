from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

# Create your views here.
def post(request):
    posts = Post.objects.all().order_by('-date')
    return render(request,'authentications/post.html', { 'posts':posts})


def postPage(request, slug):
    return HttpResponse(slug)