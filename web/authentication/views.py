from django.shortcuts import render
from .models import Post

# Create your views here.
def post(request):
    posts = Post.objects.all().order_by('-date')
    return render(request,'authentications/post.html', { 'posts':posts})
