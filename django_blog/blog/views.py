from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
data = [
        {
            "id": 1,
            "title": "Getting Started with Django",
            "author": "Tesfaye",
            "content": "Django makes it easier to build web apps quickly...",
            "published": "2025-12-01"
        },
        {
            "id": 2,
            "title": "Understanding URL Routing",
            "author": "Tesfaye",
            "content": "URL routing in Django is modular and powerful...",
            "published": "2025-12-05"
        },
        {
            "id": 3,
            "title": "Database Design Tips",
            "author": "Tesfaye",
            "content": "A clean schema design saves headaches later...",
            "published": "2025-12-10"
        }
    ]
context = {'post': data, 'page_title': 'blog'}
    


def home(request):
    return render(request,'blog/home.html', context)
def about(request):
    return render(request,'blog/about.html', {'data':'render_test'})


    
