from django.urls import path
from . import views

appName = 'posts'
# app_name = 'postPage'

urlpatterns = [
    path('',views.post, name="posts"),
    path('posts/<slug:slug>/', views.postPage, name='pages'),
    
]