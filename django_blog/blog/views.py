from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.
context = {'post': Post.objects.all(), 'page_title': 'blog'}
def home(request):
    return render(request,'blog/home.html', context)
def about(request):
    return render(request,'blog/about.html', {'data':'render_test'})


    
